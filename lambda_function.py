import json
import boto3
import os
import psycopg2
import uuid
import logging
import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from pinecone import Pinecone

# Logging settings
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS services
s3 = boto3.client("s3")

def get_pinecone_client():
    """Get Pinecone client using v6 API"""
    logger.info("Attempting to initialize Pinecone client")
    try:
        api_key = os.environ.get("PINECONE_API_KEY")
        if not api_key:
            logger.error("PINECONE_API_KEY environment variable not set")
            raise ValueError("PINECONE_API_KEY environment variable not set")
        
        # Initialize using Pinecone v6 API
        pc = Pinecone(api_key=api_key)
        logger.info("Successfully initialized Pinecone client")
        return pc
    except Exception as e:
        logger.error(f"Error connecting to Pinecone: {str(e)}")
        raise

def upload_to_postgres(documents, source_name, processed_at):
    """Upload documents to PostgreSQL database"""
    logger.info("Starting upload to PostgreSQL")
    # Get PostgreSQL connection details from environment variables
    db_host = os.environ.get("PGHOST")
    db_name = os.environ.get("PGDATABASE")
    db_user = os.environ.get("PGUSER")
    db_password = os.environ.get("PGPASSWORD")
    db_port = os.environ.get("PGPORT", "5432")
    
    logger.info(f"PostgreSQL connection details: Host={db_host}, Database={db_name}, User={db_user}, Port={db_port}")
    
    if not all([db_host, db_name, db_user, db_password]):
        logger.error(f"Missing PostgreSQL environment variables: PGHOST={db_host}, PGDATABASE={db_name}, PGUSER={db_user}, PGPASSWORD={'*' * len(db_password) if db_password else None}")
        raise ValueError("Required PostgreSQL environment variables not set")
    
    # Connect to database
    logger.info("Attempting to connect to PostgreSQL")
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=int(db_port)
    )
    
    try:
        logger.info("Connected to PostgreSQL, starting transaction")
        with conn.cursor() as cur:
            # Check if source exists
            logger.info(f"Checking if source '{source_name}' exists")
            cur.execute("SELECT id FROM sources WHERE name = %s", (source_name,))
            result = cur.fetchone()
            
            if result:
                source_id = result[0]
                logger.info(f"Found existing source: {source_name} (ID: {source_id})")
            else:
                # Get URL and description from first document
                first_doc = documents[0] if documents else None
                base_url = first_doc.metadata.get("url", f"https://{source_name}") if first_doc else f"https://{source_name}"
                description = f"{source_name} documentation"
                
                logger.info(f"Creating new source: {source_name}")
                cur.execute(
                    "INSERT INTO sources (name, base_url, description) VALUES (%s, %s, %s) RETURNING id",
                    (source_name, base_url, description)
                )
                source_id = cur.fetchone()[0]
                logger.info(f"Created new source: {source_name} (ID: {source_id})")
                conn.commit()
            
            # Add documents
            logger.info(f"Uploading {len(documents)} documents to PostgreSQL")
            for doc in documents:
                # Check missing metadata fields
                url = doc.metadata.get("url", f"https://{source_name}")
                title = doc.metadata.get("title", "Untitled Document")
                
                logger.debug(f"Inserting document: {title} ({url})")
                cur.execute(
                    "INSERT INTO documents (url, title, content, source_id, metadata, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (url, title, doc.page_content, source_id, json.dumps(doc.metadata), processed_at, processed_at)
                )
            
            conn.commit()
            logger.info(f"Successfully uploaded {len(documents)} documents to PostgreSQL")
    finally:
        logger.info("Closing PostgreSQL connection")
        conn.close()

def split_document(document):
    """Split document into chunks using LangChain"""
    logger.info("Starting document splitting")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = text_splitter.split_documents([document])
    
    doc_id = document.metadata.get("id", document.metadata.get("url", str(uuid.uuid4())))
    doc_id = doc_id.split("/")[-1] if "/" in doc_id else doc_id
    doc_id = doc_id.replace(".", "_").replace("-", "_")
    
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"{doc_id}_{i}"
        chunk.metadata["chunk_index"] = i
        chunk.metadata["total_chunks"] = len(chunks)
    
    logger.info(f"Document split into {len(chunks)} chunks")
    return chunks

def upload_to_pinecone(chunks, namespace):
    """Upload document chunks to Pinecone using the v6 API and Pinecone Inference"""
    logger.info("Starting upload to Pinecone")
    pc = get_pinecone_client()
    if not pc:
        raise ValueError("Could not initialize Pinecone client")
    
    index_name = os.environ.get("PINECONE_INDEX", "mcp-index")
    logger.info(f"Using Pinecone index: {index_name}")
    
    index = pc.Index(index_name)
    
    # Generate embeddings with Pinecone Inference
    logger.info("Generating embeddings with Pinecone Inference")
    try:
        embeddings = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[chunk.page_content for chunk in chunks],
            parameters={"input_type": "passage"}
        )
        logger.info(f"Generated {len(embeddings)} embeddings")
    except Exception as e:
        logger.error(f"Error generating embeddings with Pinecone Inference: {str(e)}")
        raise
    
    # Prepare vectors
    vectors = []
    for chunk, embedding in zip(chunks, embeddings):
        # Create metadata dictionary with all required fields
        metadata = {
            "text": chunk.page_content,
            "title": chunk.metadata.get("title", "Untitled Document"),
            "url": chunk.metadata.get("url", "#"),
            "source": namespace
        }
        
        # Add other metadata fields if they are valid types
        for k, v in chunk.metadata.items():
            if k not in ["text", "title", "url", "source"] and isinstance(v, (str, int, float, bool)):
                metadata[k] = v
        
        # Create vector ID
        vector = {
            "id": chunk.metadata["chunk_id"],
            "values": embedding["values"],
            "metadata": metadata
        }
        
        vectors.append(vector)
    
    # Upload vectors to Pinecone in batches
    if vectors:
        batch_size = 100
        logger.info(f"Preparing to upsert {len(vectors)} vectors to Pinecone")
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i+batch_size]
            try:
                index.upsert(vectors=batch, namespace=namespace)
                logger.info(f"Upserted batch of {len(batch)} vectors to Pinecone")
            except Exception as e:
                logger.error(f"Error upserting batch to Pinecone: {str(e)}")
    
    logger.info(f"Completed upload of {len(vectors)} vectors to Pinecone")
    return len(vectors)

def lambda_handler(event, context):
    """
    Lambda function that processes markdown files from S3, splits them into chunks,
    and uploads them to PostgreSQL and Pinecone.
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        processed_at = datetime.datetime.now().isoformat()
        
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]
        
        logger.info(f"Processing file: s3://{bucket}/{key}")
        
        if not key.endswith(".md") or "/md/" not in key:
            logger.info(f"Skipping non-markdown file: {key}")
            return {"statusCode": 200, "body": json.dumps({"message": "Skipped non-markdown file"})}
        
        logger.info("Parsing S3 key for domain and page ID")
        try:
            domain = key.split('/')[0]
            filename = key.split('/')[-1]
            page_id = filename[:-3]
        except Exception as e:
            logger.error(f"Error parsing key {key}: {str(e)}")
            domain = "unknown"
            page_id = f"page_{uuid.uuid4()}"
        
        md_key = key
        logger.info("Fetching markdown file from S3")
        try:
            md_file_obj = s3.get_object(Bucket=bucket, Key=md_key)
            md_content = md_file_obj["Body"].read().decode("utf-8")
            logger.info(f"Read markdown content: {len(md_content)} characters")
        except Exception as e:
            logger.error(f"Error reading markdown file {md_key}: {str(e)}")
            return {"statusCode": 500, "body": json.dumps({"error": f"Error reading markdown file: {str(e)}"})}
        
        json_key = key.replace("/md/", "/json/").replace(".md", ".json")
        logger.info("Fetching JSON metadata from S3")
        try:
            json_file_obj = s3.get_object(Bucket=bucket, Key=json_key)
            json_content = json_file_obj["Body"].read().decode("utf-8")
            metadata = json.loads(json_content)
            logger.info(f"Read JSON metadata: {len(json_content)} characters")
        except Exception as e:
            logger.error(f"Error reading JSON file {json_key}: {str(e)}")
            metadata = {"url": f"https://{domain.replace('_', '.')}", "title": page_id, "source": domain}
        
        if "url" not in metadata:
            source_url = f"https://{domain.replace('_', '.')}"
            metadata["url"] = source_url
            logger.warning(f"URL not found in metadata, using default: {source_url}")
        
        metadata["processed_at"] = processed_at
        doc = Document(page_content=md_content, metadata=metadata)
        
        source_name = domain.replace("_", ".")
        logger.info(f"Starting PostgreSQL upload for source: {source_name}")
        try:
            upload_to_postgres([doc], source_name, processed_at)
            logger.info(f"Completed PostgreSQL upload for source: {source_name}")
        except Exception as e:
            logger.error(f"Error uploading to PostgreSQL: {str(e)}")
        
        logger.info("Starting document splitting")
        try:
            chunks = split_document(doc)
            logger.info(f"Completed splitting into {len(chunks)} chunks")
        except Exception as e:
            logger.error(f"Error splitting document: {str(e)}")
            logger.warning("Creating single chunk from entire document due to splitting error")
            single_chunk = Document(
                page_content=doc.page_content,
                metadata={**doc.metadata, "chunk_id": f"{page_id}_0", "chunk_index": 0, "total_chunks": 1, "error": f"Splitting error: {str(e)}"}
            )
            chunks = [single_chunk]
        
        if chunks:
            logger.info("Starting Pinecone upload")
            try:
                uploaded_count = upload_to_pinecone(chunks, domain)
                logger.info(f"Completed Pinecone upload: {uploaded_count} chunks")
            except Exception as e:
                logger.error(f"Error uploading to Pinecone: {str(e)}")
        
        logger.info("Lambda execution completed successfully")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Processed",
                "source": source_name,
                "chunks": len(chunks),
                "page_id": page_id,
                "processed_at": processed_at
            })
        }
    except Exception as e:
        logger.error(f"Unhandled exception in lambda_handler: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}