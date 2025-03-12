#!/usr/bin/env python3
"""
Firecrawl API Documentation Crawler

This script crawls documentation websites using the Firecrawl API,
and saves the results to PostgreSQL.
"""

import os
import json
import re
import argparse
import urllib.parse
import time
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv

# Import for PostgreSQL integration
from db_utils import save_to_postgres, get_domain_name, create_tables

# Load environment variables
load_dotenv()

# Firecrawl API configuration
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
FIRECRAWL_BASE_URL = "https://api.firecrawl.dev/v1"  # v1 endpoint'ini kullan

def clean_markdown_content(markdown_content):
    """Cleans the markdown content."""
    print("Cleaning content...")
    
    # Step 1: Clean header section
    markdown_content = re.sub(r'\[.*? home page.*?\]\(https?://.*?\)', '', markdown_content, flags=re.DOTALL)
    
    # Step 2: Remove simple phrases
    patterns = [
        r'Search\.\.\.',
        r'Ctrl K',
        r'Navigation',
        r'English',
        r'Copy',
        r'Was this page helpful\?',
        r'YesNo',
        r'On this page',
        r'Try in Console',
        r'© \d{4}.*',
    ]
    
    for pattern in patterns:
        markdown_content = re.sub(pattern, '', markdown_content, flags=re.MULTILINE)
    
    # Step 3: Split content into lines and find main content
    lines = markdown_content.split('\n')
    
    # Check first 15 lines and start from the line with meaningful content
    start_index = 0
    for i, line in enumerate(lines[:20]):
        # Find the beginning of meaningful content (usually a heading or paragraph)
        if re.match(r'^#+\s+', line) or (len(line) > 30 and not re.search(r'https?://', line)):
            start_index = i
            break
    
    # If no meaningful content is found, skip the first 15 lines
    if start_index == 0 and len(lines) > 15:
        start_index = 15
    
    # Create new content
    markdown_content = '\n'.join(lines[start_index:])
    
    # Step 4: Empty link text links
    markdown_content = re.sub(r'\[\]\(https?://[^\)]+\)', '', markdown_content)
    
    # Step 5: Clean heading links but keep headings
    markdown_content = re.sub(r'\[​\]\(https?://[^\)]+\)', '', markdown_content)
    
    # Step 6: Clean empty lines and extra spaces
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    markdown_content = re.sub(r' {2,}', ' ', markdown_content)
    
    # Step 7: Clean empty bullet points
    markdown_content = re.sub(r'- \n', '', markdown_content)
    
    # Final cleanup
    markdown_content = markdown_content.strip()
    
    return markdown_content

def fix_markdown_line_breaks(markdown_content):
    """Correct line breaks in Markdown content and clean up trailing characters."""
    # Fix Windows-style line breaks
    fixed_markdown = markdown_content.replace('\r\n', '\n')
    
    # Ensure consistent line breaks for paragraphs
    fixed_markdown = re.sub(r'([^\n])\n([^\n])', r'\1 \2', fixed_markdown)
    
    # Remove any trailing % characters and whitespace
    fixed_markdown = fixed_markdown.rstrip('%\n\t ')
    
    return fixed_markdown

def check_api_key():
    """Check if Firecrawl API key is available."""
    if not FIRECRAWL_API_KEY:
        raise ValueError("FIRECRAWL_API_KEY is not set in .env file")
    return True

def crawl_with_firecrawl(url: str, limit: int = 100, max_depth: int = 3):
    """Crawl website using Firecrawl API."""
    print(f"Starting Firecrawl crawl of {url} with limit {limit} and max_depth {max_depth}")
    
    # Check API key
    check_api_key()
    
    # Create the API request payload
    payload = {
        "url": url,
        "limit": limit,
        "maxDepth": max_depth,
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True
        },
        "ignoreSitemap": False,
        "allowExternalLinks": False
    }
    
    # API request headers
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Make the API request
    try:
        print("Sending request to Firecrawl API...")
        response = requests.post(
            f"{FIRECRAWL_BASE_URL}/crawl",
            json=payload,
            headers=headers
        )
        
        # Check for successful response
        response.raise_for_status()
        
        # Get crawl job ID
        crawl_data = response.json()
        print(f"Response: {crawl_data}")
        
        crawl_id = crawl_data.get("id")
        
        if not crawl_id:
            raise Exception("No crawl ID returned from API")
        
        print(f"Crawl job initiated with ID: {crawl_id}")
        
        # Poll for crawl completion
        return poll_crawl_status(crawl_id)
        
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        if hasattr(e, 'response') and e.response:
            print(f"Response status: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        raise

def poll_crawl_status(crawl_id: str, interval: int = 5, timeout: int = 600):
    """Poll for crawl completion and return results."""
    print(f"Polling for crawl completion (ID: {crawl_id})...")
    
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # Get crawl status
            status_url = f"{FIRECRAWL_BASE_URL}/crawl/{crawl_id}"
            print(f"Checking status at: {status_url}")
            
            response = requests.get(
                status_url,
                headers=headers
            )
            
            response.raise_for_status()
            status_data = response.json()
            
            print(f"Status response: {status_data}")
            
            job_status = status_data.get("status")
            print(f"Current status: {job_status}")
            
            # Check if completed or failed
            if job_status == "completed":
                print("Crawl completed successfully!")
                
                # Get the results
                results_response = requests.get(
                    f"{FIRECRAWL_BASE_URL}/crawl/{crawl_id}",
                    headers=headers
                )
                
                results_response.raise_for_status()
                results_data = results_response.json()
                
                # Process and return the results
                return process_firecrawl_results(results_data)
                
            elif job_status in ["failed", "cancelled"]:
                error_message = status_data.get("error", "Unknown error")
                raise Exception(f"Crawl failed: {error_message}")
            
            # Wait before next poll
            time.sleep(interval)
            
        except requests.exceptions.RequestException as e:
            print(f"Error polling crawl status: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Response status: {e.response.status_code}")
                print(f"Response text: {e.response.text}")
            time.sleep(interval)
    
    # If we get here, we've timed out
    raise Exception(f"Crawl polling timed out after {timeout} seconds")

def process_firecrawl_results(results_data):
    """Process Firecrawl API results into the same format as local crawler."""
    print("Processing Firecrawl results...")
    print(f"Results data keys: {list(results_data.keys())}")
    
    processed_results = []
    
    # The data structure might be different than expected
    # Check if 'data' key exists in results_data
    if 'data' in results_data:
        # Extract pages from data field
        pages = results_data.get('data', [])
        print(f"Found {len(pages)} pages in data field")
        
        for page in pages:
            # Check if this is a page object with markdown content
            if isinstance(page, dict) and 'markdown' in page and 'metadata' in page:
                processed_results.append(page)
            elif isinstance(page, dict) and 'content' in page:
                # Content might be directly in the page
                url = page.get('url', '')
                title = page.get('title', '')
                
                # Content might be in different formats
                content = ''
                if isinstance(page['content'], dict) and 'markdown' in page['content']:
                    content = page['content']['markdown']
                elif isinstance(page['content'], str):
                    content = page['content']
                
                # Clean up markdown content
                cleaned_content = clean_markdown_content(content)
                fixed_content = fix_markdown_line_breaks(cleaned_content)
                
                # Create metadata similar to local crawler
                metadata = {
                    "sourceURL": url,
                    "title": title,
                    "crawlTime": page.get("timestamp"),
                    "statusCode": page.get("statusCode", 200)
                }
                
                # Add to processed results
                processed_results.append({
                    "markdown": fixed_content,
                    "metadata": metadata
                })
    
    # If we still don't have results, try to extract pages directly
    if not processed_results and 'pages' in results_data:
        pages = results_data.get('pages', [])
        print(f"Found {len(pages)} pages in pages field")
        
        for page in pages:
            url = page.get('url', '')
            title = page.get('title', '')
            
            # Content might be in different formats
            content = ''
            if isinstance(page.get('content'), dict) and 'markdown' in page['content']:
                content = page['content']['markdown']
            elif isinstance(page.get('content'), str):
                content = page['content']
            
            if content:
                # Clean up markdown content
                cleaned_content = clean_markdown_content(content)
                fixed_content = fix_markdown_line_breaks(cleaned_content)
                
                # Create metadata similar to local crawler
                metadata = {
                    "sourceURL": url,
                    "title": title,
                    "crawlTime": page.get("timestamp"),
                    "statusCode": page.get("statusCode", 200)
                }
                
                # Add to processed results
                processed_results.append({
                    "markdown": fixed_content,
                    "metadata": metadata
                })
    
    print(f"Processed {len(processed_results)} results")
    return processed_results

def chunk_text(text, max_chars=1500):
    """Split text into smaller chunks for vectorization."""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) < max_chars:
            current_chunk += paragraph + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def init_pinecone():
    """Initialize connection to Pinecone."""
    try:
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not pinecone_api_key:
            print("PINECONE_API_KEY not found in environment variables.")
            return None
            
        # Direct connection to the index host from the dashboard
        host = "https://mcp-index-3jg9lch.svc.aped-4627-b74a.pinecone.io"
        
        # Test connection by getting index stats
        headers = {
            "Api-Key": pinecone_api_key,
            "Accept": "application/json"
        }
        
        # Try to get index stats
        stats_url = f"{host}/describe_index_stats"
        response = requests.post(stats_url, headers=headers, json={})
        
        if response.status_code == 200:
            print("Successfully connected to Pinecone index!")
            print(f"Index stats: {response.json()}")
            
            # Return a dictionary with the host and headers for later use
            return {
                "host": host,
                "headers": headers
            }
        else:
            print(f"Connection to Pinecone failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error initializing Pinecone: {e}")
        return None

def upload_to_pinecone(source_name, documents):
    """Upload documents to Pinecone vector database."""
    pinecone_conn = init_pinecone()
    if not pinecone_conn:
        print("Failed to initialize Pinecone connection.")
        return
    
    host = pinecone_conn["host"]
    headers = pinecone_conn["headers"]
    upsert_url = f"{host}/vectors/upsert"
    
    print(f"Uploading documents to Pinecone (source: {source_name})")
    
    # Create namespace from source name (replace invalid characters)
    namespace = re.sub(r'[^a-zA-Z0-9_-]', '_', source_name.lower())
    
    # Process documents in batches
    batch_size = 100
    count = 0
    total_vectors = 0
    
    for doc in documents:
        # Skip documents without markdown content
        if 'markdown' not in doc or not doc['markdown']:
            print(f"Skipping document without markdown content: {doc.get('metadata', {}).get('sourceURL', 'unknown')}")
            continue
            
        # Get chunks of text
        chunks = chunk_text(doc['markdown'])
        
        # Extract metadata from document
        title = doc.get('metadata', {}).get('title', '')
        url = doc.get('metadata', {}).get('sourceURL', '')
        
        # Try direct access if metadata doesn't have the fields
        if not title and 'title' in doc:
            title = doc['title']
        if not url and 'url' in doc:
            url = doc['url']
            
        # For multilingual-e5-large model, we need 1024 dimensions
        dim = 1024
        
        # Process chunks in batches
        vectors_batch = []
        
        for i, chunk in enumerate(chunks):
            doc_id = f"{url.replace('://', '_').replace('/', '_')}_{i}"
            
            # Create a mock embedding vector
            # Note: In a production environment, you would use an actual embedding model
            mock_embedding = [0.01] * dim
            
            # Ensure all required metadata fields are present
            metadata = {
                "title": title or "Untitled Document",
                "url": url or "#",
                "chunk_index": i,
                "text": chunk,  # Use 'text' field as specified in Pinecone dashboard
                "source": source_name
            }
            
            # Add additional metadata fields if available
            if 'markdown' in doc:
                metadata["markdown"] = doc['markdown'][:1000]  # Limit size to avoid exceeding metadata limits
            
            vectors_batch.append({
                "id": doc_id,
                "values": mock_embedding,
                "metadata": metadata
            })
            
            # Upload in batches
            if len(vectors_batch) >= batch_size:
                try:
                    upsert_data = {
                        "vectors": vectors_batch,
                        "namespace": namespace
                    }
                    
                    response = requests.post(upsert_url, headers=headers, json=upsert_data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        print(f"Uploaded {result.get('upsertedCount', len(vectors_batch))} vectors to Pinecone.")
                        total_vectors += result.get('upsertedCount', len(vectors_batch))
                    else:
                        print(f"Error uploading vectors to Pinecone: {response.status_code} - {response.text}")
                        
                    vectors_batch = []
                except Exception as e:
                    print(f"Error uploading vectors to Pinecone: {e}")
        
        count += 1
        
    # Upload any remaining vectors
    if vectors_batch:
        try:
            upsert_data = {
                "vectors": vectors_batch,
                "namespace": namespace
            }
            
            response = requests.post(upsert_url, headers=headers, json=upsert_data)
            
            if response.status_code == 200:
                result = response.json()
                print(f"Uploaded final {result.get('upsertedCount', len(vectors_batch))} vectors to Pinecone.")
                total_vectors += result.get('upsertedCount', len(vectors_batch))
            else:
                print(f"Error uploading final vectors to Pinecone: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error uploading remaining vectors to Pinecone: {e}")
            
    print(f"Completed uploading {total_vectors} vectors to Pinecone namespace: {namespace}")

def save_crawl_results(results, base_url):
    """Saves crawl results to files and PostgreSQL."""
    if not results:
        print("No data to save!")
        return
    
    # Create docs directory
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    
    # Get domain name
    domain_name = get_domain_name(base_url)
    
    # Create directory for domain
    domain_dir = docs_dir / domain_name
    domain_dir.mkdir(exist_ok=True)
    
    # Save each page
    for page in results:
        if "markdown" in page and "metadata" in page and "sourceURL" in page["metadata"]:
            url = page["metadata"]["sourceURL"]
            markdown_content = page["markdown"]
            
            # Create filename
            parsed_url = urlparse(url)
            path = parsed_url.path.strip("/")
            
            if not path:
                filename = f"{domain_name}_index"
            else:
                # Convert URL path to filename
                filename = path.replace("/", "_").replace(".", "_")
                
                # Shorten very long filenames
                if len(filename) > 100:
                    filename = filename[:100]
                
                filename = f"{domain_name}_{filename}"
            
            # Save JSON file
            json_path = domain_dir / f"{filename}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump({
                    "content": markdown_content,
                    "metadata": page["metadata"]
                }, f, ensure_ascii=False, indent=2)
            
            # Save Markdown file
            md_path = domain_dir / f"{filename}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            
            print(f"Saved files: {filename}.json, {filename}.md")
    
    # Save full crawl result
    crawl_result_path = domain_dir / "crawl_result.json"
    with open(crawl_result_path, "w", encoding="utf-8") as f:
        json.dump({
            "data": results,
            "totalCount": len(results)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"All files saved to '{domain_dir}' directory.")
    print(f"Full crawl result saved to '{crawl_result_path}'")
    
    # Save to PostgreSQL
    try:
        saved_count = save_to_postgres(results, base_url)
        print(f"Saved {saved_count} documents to PostgreSQL database.")
        
        # Upload to Pinecone
        upload_to_pinecone(domain_name, results)
    except Exception as e:
        print(f"Error saving to PostgreSQL: {str(e)}")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Crawl websites using Firecrawl API.")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("--limit", type=int, default=100, help="Maximum number of pages to crawl (default: 100)")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth to crawl (default: 3)")
    
    args = parser.parse_args()
    
    # Create database tables if they don't exist
    try:
        create_tables()
        print("Database tables created/verified.")
    except Exception as e:
        print(f"Warning: Failed to create/verify database tables: {e}")
    
    # Start crawl
    start_time = time.time()
    
    try:
        # Crawl with Firecrawl API
        results = crawl_with_firecrawl(args.url, args.limit, args.max_depth)
        
        # Save results
        save_crawl_results(results, args.url)
        
        end_time = time.time()
        print(f"Crawl completed in {end_time - start_time:.2f} seconds.")
        print(f"Total pages crawled: {len(results)}")
    except Exception as e:
        print(f"Error during crawl: {str(e)}")

if __name__ == "__main__":
    main() 