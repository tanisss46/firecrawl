import os
import json
import glob
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
import logging
import psycopg2
from psycopg2.extras import execute_values
import requests
import time
from pinecone import Pinecone

# LangChain importları
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
import numpy as np

# Loglama ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Çevre değişkenlerini yükle
load_dotenv()

# Pinecone'a bağlan
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX_NAME", "mcp-index")

if api_key:
    pc = Pinecone(api_key=api_key)
    logger.info(f"Pinecone'a bağlandı")
else:
    logger.warning("PINECONE_API_KEY çevre değişkeni ayarlanmamış")
    pc = None

# Dokümanları yükle
def load_documents(docs_dir: str, source_name: str) -> List[Document]:
    documents = []
    
    # JSON dosyalarını bul
    json_files = glob.glob(os.path.join(docs_dir, f"{source_name}_*.json"))
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Markdown dosyasını da bul
                md_file = json_file.replace('.json', '.md')
                
                if os.path.exists(md_file):
                    with open(md_file, 'r', encoding='utf-8') as md_f:
                        content = md_f.read()
                        
                        # Metadata'yı çıkar
                        metadata = data.get("metadata", {})
                        
                        # Doküman oluştur
                        doc = Document(
                            page_content=content,
                            metadata={
                                "source": source_name,
                                "url": metadata.get("url", ""),
                                "title": metadata.get("title", ""),
                                "description": metadata.get("description", ""),
                                "id": os.path.basename(json_file)
                            }
                        )
                        
                        documents.append(doc)
        except Exception as e:
            logger.error(f"Doküman yükleme hatası ({json_file}): {str(e)}")
    
    logger.info(f"{source_name} için {len(documents)} doküman yüklendi")
    return documents

# Ham dokümanları PostgreSQL'e yükle (parçalamadan)
def upload_raw_to_postgres(documents: List[Document], source_name: str):
    try:
        # Veritabanı bağlantısı
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "docs_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            port=os.getenv("DB_PORT", 5432)
        )
        
        # Kaynak ID'sini al veya oluştur
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM sources WHERE name = %s", (source_name,))
            result = cur.fetchone()
            
            if result:
                source_id = result[0]
            else:
                # Kaynak URL'sini belirle
                base_url = "https://modelcontextprotocol.io"
                if source_name == "react_dev":
                    base_url = "https://react.dev"
                elif source_name == "docs_python_org":
                    base_url = "https://docs.python.org"
                elif source_name == "tailwindcss_com":
                    base_url = "https://tailwindcss.com"
                elif source_name == "docs_vendure_io":
                    base_url = "https://docs.vendure.io"
                
                cur.execute(
                    "INSERT INTO sources (name, base_url, description) VALUES (%s, %s, %s) RETURNING id", 
                    (source_name, base_url, f"{source_name} documentation")
                )
                source_id = cur.fetchone()[0]
                conn.commit()
        
        # Ham dokümanları ekle
        with conn.cursor() as cur:
            for doc in documents:
                metadata = doc.metadata
                url = metadata.get("url", "")
                title = metadata.get("title", "")
                
                # Metadata'yı JSON olarak hazırla
                json_metadata = {
                    "description": metadata.get("description", ""),
                    "id": metadata.get("id", ""),
                    "source": metadata.get("source", source_name)
                }
                
                cur.execute(
                    """
                    INSERT INTO documents (url, title, content, source_id, metadata)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (url) DO UPDATE SET
                        title = EXCLUDED.title,
                        content = EXCLUDED.content,
                        metadata = EXCLUDED.metadata,
                        updated_at = CURRENT_TIMESTAMP
                    """,
                    (url, title, doc.page_content, source_id, json.dumps(json_metadata))
                )
            
            conn.commit()
        
        # Doküman sayısını güncelle
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE sources
                SET document_count = (SELECT COUNT(*) FROM documents WHERE source_id = %s),
                    last_crawled = CURRENT_TIMESTAMP
                WHERE id = %s
                """,
                (source_id, source_id)
            )
            conn.commit()
        
        logger.info(f"{len(documents)} ham doküman PostgreSQL'e yüklendi")
    except Exception as e:
        logger.error(f"PostgreSQL ham yükleme hatası: {str(e)}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()

# Dokümanları parçala
def split_documents(documents: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    
    chunks = text_splitter.split_documents(documents)
    logger.info(f"{len(documents)} doküman, {len(chunks)} parçaya bölündü")
    return chunks

# Pinecone Cloud Inference API ile vektör oluştur
def create_embeddings_with_pinecone(texts: List[str], model_name: str = "multilingual-e5-large"):
    try:
        if pc is None:
            raise ValueError("Pinecone bağlantısı kurulmamış")
            
        # Batch işleme için maksimum boyut
        batch_size = 50
        all_embeddings = []
        
        # Metinleri batch'lere böl
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            try:
                logger.info(f"Pinecone Inference API'ye istek gönderiliyor: {i+1}-{i+len(batch)}/{len(texts)}")
                
                # Pinecone Cloud Inference API ile embeddings oluştur
                response = pc.inference.embed(
                    model=model_name,
                    inputs=batch,
                    parameters={"input_type": "passage"}
                )
                
                # Yanıtı işle
                all_embeddings.extend(response)
                
                # API rate limit'i aşmamak için kısa bir bekleme
                time.sleep(0.5)
                
            except Exception as e:
                logger.error(f"Pinecone Inference API hatası (batch {i+1}-{i+len(batch)}): {str(e)}")
                raise
        
        logger.info(f"Toplam {len(all_embeddings)} vektör oluşturuldu")
        return all_embeddings
    except Exception as e:
        logger.error(f"Pinecone Inference API hatası: {str(e)}")
        raise

# Pinecone'a yükle
def upload_to_pinecone(chunks: List[Document], namespace: str):
    try:
        if pc is None:
            raise ValueError("Pinecone bağlantısı kurulmamış")
            
        # Pinecone indeksini kontrol et
        if index_name not in pc.list_indexes().names():
            logger.error(f"'{index_name}' indeksi bulunamadı")
            raise ValueError(f"'{index_name}' indeksi bulunamadı")
        
        # İndekse bağlan
        index = pc.Index(index_name)
        
        # Doküman içeriklerini çıkar
        texts = [chunk.page_content for chunk in chunks]
        
        # Pinecone Cloud Inference API ile vektör oluştur
        embeddings = create_embeddings_with_pinecone(texts, "multilingual-e5-large")
        
        # Batch işleme için maksimum boyut
        batch_size = 100
        
        # Vektörleri batch'lere böl
        for i in range(0, len(chunks), batch_size):
            batch_chunks = chunks[i:i + batch_size]
            batch_embeddings = embeddings[i:i + batch_size]
            
            vectors = []
            for j, (chunk, embedding) in enumerate(zip(batch_chunks, batch_embeddings)):
                # Metadata hazırla
                metadata = {}
                
                # Gerekli metadata alanlarını ekle
                metadata["text"] = chunk.page_content
                metadata["title"] = chunk.metadata.get("title", "Untitled Document")
                metadata["url"] = chunk.metadata.get("url", "#")
                metadata["source"] = namespace
                
                # Diğer metadata alanlarını ekle
                for k, v in chunk.metadata.items():
                    if k not in ["text", "title", "url", "source"] and isinstance(v, (str, int, float, bool)):
                        metadata[k] = v
                
                # Vektör ID'si oluştur
                vector_id = f"{namespace}_{i+j}"
                
                # Vektör oluştur
                vector = {
                    "id": vector_id,
                    "values": embedding["values"],
                    "metadata": metadata
                }
                
                vectors.append(vector)
            
            # Pinecone'a yükle
            try:
                logger.info(f"Pinecone'a vektör yükleniyor: {i+1}-{i+len(batch_chunks)}/{len(chunks)}")
                index.upsert(vectors=vectors, namespace=namespace)
                
                # API rate limit'i aşmamak için kısa bir bekleme
                time.sleep(0.5)
                
            except Exception as e:
                logger.error(f"Pinecone vektör yükleme hatası (batch {i+1}-{i+len(batch_chunks)}): {str(e)}")
                raise
        
        logger.info(f"{len(chunks)} parça {namespace} namespace'ine yüklendi")
    except Exception as e:
        logger.error(f"Pinecone yükleme hatası: {str(e)}")
        raise

# Ana fonksiyon
def main():
    # Kaynak adı ve doküman dizini
    source_name = "modelcontextprotocol_io"
    docs_dir = os.path.join("docs", source_name)
    
    # 1. Dokümanları yükle
    documents = load_documents(docs_dir, source_name)
    
    # 2. Ham dokümanları PostgreSQL'e yükle (parçalamadan)
    upload_raw_to_postgres(documents, source_name)
    
    # 3. Dokümanları parçala
    chunks = split_documents(documents)
    
    # 4. Parçaları Pinecone'a yükle (vektörleştirerek)
    upload_to_pinecone(chunks, source_name)
    
    logger.info("İşlem tamamlandı")

if __name__ == "__main__":
    main() 