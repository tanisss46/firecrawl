# firecrawl_to_s3.py
import boto3
import json
import os
import logging
import argparse
import time
import re
from urllib.parse import urlparse
from dotenv import load_dotenv
import requests

# Loglama ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Çevre değişkenlerini yükle
load_dotenv()

# API anahtarlarını al
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def upload_to_s3(content, bucket_name, object_name, content_type='text/plain', aws_access_key=None, aws_secret_key=None, aws_region=None):
    """
    Bellek içindeki içeriği doğrudan S3 bucket'a yükler
    """
    # S3 istemcisi oluştur
    s3_kwargs = {}
    if aws_access_key and aws_secret_key:
        s3_kwargs['aws_access_key_id'] = aws_access_key
        s3_kwargs['aws_secret_access_key'] = aws_secret_key
    if aws_region:
        s3_kwargs['region_name'] = aws_region
    
    s3 = boto3.client("s3", **s3_kwargs)
    
    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=content.encode("utf-8"),
            ContentType=content_type
        )
        logger.info(f"{object_name} S3'e yüklendi")
        return True
    except Exception as e:
        logger.error(f"S3 yükleme hatası: {str(e)}")
        return False

def start_crawl_with_firecrawl(url, limit=None):
    """
    Firecrawl API ile URL'yi crawl etmeye başlar ve job ID döndürür
    """
    api_url = "https://api.firecrawl.dev/v1/crawl"
    
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "url": url,
        "limit": limit
    }
    
    try:
        logger.info(f"Firecrawl API'ye istek gönderiliyor: {url}")
        logger.debug(f"Request payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(api_url, headers=headers, json=payload)
        
        try:
            result = response.json()
            logger.debug(f"Response: {json.dumps(result, indent=2)}")
        except:
            logger.error(f"Response text: {response.text}")
            return None
        
        response.raise_for_status()
        
        if "id" in result:
            job_id = result["id"]
            logger.info(f"Firecrawl crawl işi başlatıldı, ID: {job_id}")
            return job_id
        else:
            logger.error("Firecrawl API yanıtında job ID bulunamadı")
            return None
    except Exception as e:
        logger.error(f"Firecrawl API hatası: {str(e)}")
        return None

def check_crawl_status(job_id):
    """
    Firecrawl API ile crawl işinin durumunu kontrol eder
    """
    api_url = f"https://api.firecrawl.dev/v1/crawl/{job_id}"
    
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return result
    except Exception as e:
        logger.error(f"Crawl durumu kontrol hatası: {str(e)}")
        return None

def get_page_id_from_url(url, base_url, index):
    """
    URL'den sayfa ID'si oluşturur
    """
    if not url:
        return f"doc_{index}"
    
    try:
        # URL'yi parse et
        parsed_url = urlparse(url)
        
        # Domain'i al ve temizle (örn: docs.vendure.io -> docs_vendure_io)
        domain = parsed_url.netloc.replace(".", "_")
        
        # Base URL'nin domain'ini al
        base_parsed = urlparse(base_url)
        base_domain = base_parsed.netloc
        
        # Path'i al ve temizle
        path = parsed_url.path.strip("/")
        
        # Özel karakterleri temizle
        path = re.sub(r'[^a-zA-Z0-9/]', '_', path)
        
        # Slash'ları alt çizgi ile değiştir
        path = path.replace("/", "_")
        
        # Eğer aynı domain'deyse, sadece path'i kullan
        if parsed_url.netloc == base_domain:
            page_id = f"{domain}" if not path else f"{domain}_{path}"
        else:
            # Farklı domain ise, tam URL'yi ID olarak kullan
            page_id = f"{domain}_{path}"
        
        # Çoklu alt çizgileri tek alt çizgiye dönüştür
        page_id = re.sub(r'_+', '_', page_id)
        
        # Çok uzunsa kısalt
        if len(page_id) > 200:
            page_id = page_id[:200]
        
        return page_id
    except Exception as e:
        logger.warning(f"URL'den ID oluşturma hatası: {str(e)}, fallback ID kullanılıyor")
        return f"doc_{index}"

def crawl_and_upload_to_s3(url, bucket_name, limit=None, aws_access_key=None, aws_secret_key=None, aws_region=None):
    """
    URL'yi crawl eder ve sonuçları doğrudan S3'e yükler
    """
    # Base URL'den ana klasör adını belirle
    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc.replace(".", "_")
    
    # Crawl işlemini başlat
    job_id = start_crawl_with_firecrawl(url, limit)
    
    if not job_id:
        logger.error("Crawl işi başlatılamadı")
        return False
    
    # Crawl işinin tamamlanmasını bekle
    logger.info("Crawl işi başlatıldı, sonuçlar bekleniyor...")
    max_attempts = 30
    attempt = 0
    results = None
    
    while attempt < max_attempts:
        attempt += 1
        logger.info(f"Crawl durumu kontrol ediliyor (deneme {attempt}/{max_attempts})...")
        
        status_result = check_crawl_status(job_id)
        
        if not status_result:
            logger.error("Crawl durumu alınamadı")
            time.sleep(10)
            continue
        
        # Crawl tamamlandı mı kontrol et
        if "data" in status_result and status_result.get("data"):
            results = status_result.get("data")
            logger.info(f"Crawl tamamlandı, {len(results)} sayfa bulundu")
            break
        
        # Eğer next parametresi varsa, daha fazla veri var demektir
        if "next" in status_result:
            logger.info("Crawl devam ediyor, daha fazla veri bekleniyor...")
        
        # 10 saniye bekle ve tekrar kontrol et
        time.sleep(10)
    
    if not results:
        logger.error("Crawl sonuçları alınamadı veya boş")
        return False
    
    # Sonuçları S3'e yükle
    for i, result in enumerate(results):
        # Metadata'dan URL bilgisini al
        metadata = result.get("metadata", {})
        page_url = metadata.get("url", "")
        
        # URL yoksa sourceURL'yi kontrol et
        if not page_url:
            page_url = metadata.get("sourceURL", "")
        
        # Hala URL yoksa fallback kullan
        if not page_url:
            page_url = ""
        
        # URL'den ID oluştur
        page_id = get_page_id_from_url(page_url, url, i)
        
        # JSON dosyasını yükle
        json_content = json.dumps(result, ensure_ascii=False, indent=2)
        json_object_name = f"{base_domain}/json/{page_id}.json"
        upload_to_s3(
            content=json_content, 
            bucket_name=bucket_name, 
            object_name=json_object_name, 
            content_type='application/json',
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_region=aws_region
        )
        
        # MD dosyasını yükle
        md_content = result.get("markdown", "")
        md_object_name = f"{base_domain}/md/{page_id}.md"
        upload_to_s3(
            content=md_content, 
            bucket_name=bucket_name, 
            object_name=md_object_name, 
            content_type='text/markdown',
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_region=aws_region
        )
    
    logger.info(f"Toplam {len(results)} sayfa S3'e yüklendi")
    return True

def main():
    # Argüman parser'ı oluştur
    parser = argparse.ArgumentParser(description='Firecrawl ile URL crawl edip S3\'e yükle')
    parser.add_argument('--url', type=str, default="https://modelcontextprotocol.io", help='Crawl edilecek URL')
    parser.add_argument('--limit', type=int, default=50, help='Crawl edilecek maksimum sayfa sayısı')
    parser.add_argument('--bucket', type=str, default=os.getenv("S3_BUCKET_NAME", "mcp-firecrawl-data"), help='S3 bucket adı')
    parser.add_argument('--aws-access-key', type=str, default=os.getenv("AWS_ACCESS_KEY_ID"), help='AWS Access Key ID')
    parser.add_argument('--aws-secret-key', type=str, default=os.getenv("AWS_SECRET_ACCESS_KEY"), help='AWS Secret Access Key')
    parser.add_argument('--aws-region', type=str, default=os.getenv("AWS_REGION", "us-east-1"), help='AWS Region')
    
    args = parser.parse_args()
    
    # Crawl ve S3'e yükleme işlemini başlat
    crawl_and_upload_to_s3(
        url=args.url,
        bucket_name=args.bucket,
        limit=args.limit,
        aws_access_key=args.aws_access_key,
        aws_secret_key=args.aws_secret_key,
        aws_region=args.aws_region
    )

if __name__ == "__main__":
    main() 