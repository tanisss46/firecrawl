#!/usr/bin/env python3
"""
Firecrawl Documentation Crawler

This script demonstrates how to use Firecrawl to crawl a documentation website
and extract its content in a format suitable for further processing.
"""

import os
import json
import time
from firecrawl.firecrawl import FirecrawlApp

# Replace with your Firecrawl API key
FIRECRAWL_API_KEY = "fc-YOUR_API_KEY"

# Initialize the Firecrawl app
app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

def crawl_documentation(url, output_dir="crawled_docs", limit=100):
    """
    Crawl a documentation website and save the results to files.
    
    Args:
        url (str): The URL of the documentation website to crawl.
        output_dir (str): Directory to save the crawled content.
        limit (int): Maximum number of pages to crawl.
    
    Returns:
        dict: The crawl result data.
    """
    print(f"Starting to crawl {url}...")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Set crawl parameters
    params = {
        "limit": limit,
        "scrapeOptions": {
            "formats": ["markdown", "html"],
            "onlyMainContent": True  # Exclude headers, footers, etc.
        }
    }
    
    # Start the crawl job
    crawl_result = app.crawl_url(url, params, poll_interval=30)
    
    # Save the full crawl result
    with open(f"{output_dir}/crawl_result.json", "w") as f:
        json.dump(crawl_result, f, indent=2)
    
    # Save individual pages
    if "data" in crawl_result:
        for i, page in enumerate(crawl_result["data"]):
            # Create a safe filename from the URL
            if "metadata" in page and "sourceURL" in page["metadata"]:
                filename = page["metadata"]["sourceURL"].replace("://", "_").replace("/", "_").replace(".", "_")
            else:
                filename = f"page_{i}"
            
            # Save markdown content
            if "markdown" in page:
                with open(f"{output_dir}/{filename}.md", "w") as f:
                    f.write(page["markdown"])
            
            # Save HTML content
            if "html" in page:
                with open(f"{output_dir}/{filename}.html", "w") as f:
                    f.write(page["html"])
            
            # Save metadata
            if "metadata" in page:
                with open(f"{output_dir}/{filename}_metadata.json", "w") as f:
                    json.dump(page["metadata"], f, indent=2)
    
    print(f"Crawl completed. Crawled {len(crawl_result.get('data', []))} pages.")
    print(f"Results saved to {output_dir}/")
    
    return crawl_result

def map_documentation(url, output_file="site_map.json"):
    """
    Map a documentation website to get all URLs.
    
    Args:
        url (str): The URL of the documentation website to map.
        output_file (str): File to save the mapped URLs.
    
    Returns:
        dict: The map result data.
    """
    print(f"Mapping {url}...")
    
    # Map the website
    map_result = app.map_url(url)
    
    # Save the map result
    with open(output_file, "w") as f:
        json.dump(map_result, f, indent=2)
    
    print(f"Mapping completed. Found {len(map_result.get('links', []))} URLs.")
    print(f"Results saved to {output_file}")
    
    return map_result

def extract_structured_data(url, schema=None, prompt=None, output_file="extracted_data.json"):
    """
    Extract structured data from a documentation website.
    
    Args:
        url (str): The URL of the documentation website to extract data from.
        schema (dict, optional): JSON schema for structured data extraction.
        prompt (str, optional): Natural language prompt for extraction.
        output_file (str): File to save the extracted data.
    
    Returns:
        dict: The extraction result data.
    """
    print(f"Extracting structured data from {url}...")
    
    # Set extraction parameters
    params = {}
    if schema:
        params["schema"] = schema
    if prompt:
        params["prompt"] = prompt
    
    # Extract data
    extract_result = app.extract([url], params)
    
    # Save the extraction result
    with open(output_file, "w") as f:
        json.dump(extract_result, f, indent=2)
    
    print(f"Extraction completed.")
    print(f"Results saved to {output_file}")
    
    return extract_result

def main():
    """Main function to demonstrate Firecrawl usage."""
    # Example: Crawl Vendure documentation
    docs_url = "https://docs.vendure.io"
    
    # First, map the website to get all URLs
    map_result = map_documentation(docs_url)
    
    # Then, crawl the documentation
    crawl_result = crawl_documentation(docs_url, limit=50)
    
    # Example: Extract structured data with a prompt
    extraction_prompt = "Extract all API endpoints, their parameters, and descriptions from the documentation."
    extract_result = extract_structured_data(
        docs_url, 
        prompt=extraction_prompt,
        output_file="vendure_api_endpoints.json"
    )

if __name__ == "__main__":
    main() 