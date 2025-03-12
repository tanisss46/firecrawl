#!/usr/bin/env python3
"""
Fix metadata issues in Pinecone vectors.
This script will:
1. Connect to Pinecone
2. List available namespaces
3. Query vectors from each namespace
4. Fix metadata issues by updating vectors with correct metadata structure
"""

import os
import requests
import json
import argparse
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Pinecone credentials from environment
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_HOST = os.getenv("PINECONE_HOST")

if not PINECONE_API_KEY or not PINECONE_HOST:
    raise ValueError("PINECONE_API_KEY and PINECONE_HOST must be set in the .env file")

def pinecone_request(endpoint, method="GET", data=None):
    """Send a direct request to the Pinecone API"""
    url = f"https://{PINECONE_HOST}/{endpoint}"
    
    headers = {
        "Api-Key": PINECONE_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        print(f"Sending Pinecone API request: {method} {url}")
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Pinecone API request error: {str(e)}")
        if 'response' in locals():
            print(f"Response content: {response.text if hasattr(response, 'text') else 'No response'}")
        raise

def list_namespaces():
    """List all available namespaces in the Pinecone index"""
    try:
        response = pinecone_request("describe_index_stats")
        namespaces = response.get("namespaces", {})
        
        result = []
        for ns_name, ns_data in namespaces.items():
            result.append({
                "name": ns_name,
                "vector_count": ns_data.get("vector_count", 0)
            })
        
        return result
    except Exception as e:
        print(f"Error listing namespaces: {str(e)}")
        raise

def check_metadata_fields(metadata):
    """Check if the metadata contains the expected fields"""
    expected_fields = ["text", "title", "url", "source"]
    missing_fields = [field for field in expected_fields if field not in metadata]
    
    if missing_fields:
        return False, f"Missing metadata fields: {', '.join(missing_fields)}"
    
    # Check if text field is not empty
    if not metadata.get("text"):
        return False, "Metadata 'text' field is empty"
    
    return True, "All metadata fields are present and valid"

def query_vectors_in_namespace(namespace, top_k=100):
    """Query vectors in a specific namespace"""
    try:
        # Use a simple query vector (all zeros)
        query_vector = [0.0] * 1024  # Assuming 1024-dimensional vectors
        
        # Query Pinecone
        data = {
            "vector": query_vector,
            "topK": top_k,
            "includeMetadata": True,
            "includeValues": True,
            "namespace": namespace
        }
        
        response = pinecone_request("query", method="POST", data=data)
        
        # Check results
        matches = response.get("matches", [])
        if not matches:
            print(f"No vectors found in namespace '{namespace}'")
            return []
        
        results = []
        for i, match in enumerate(matches):
            vector_id = match.get("id", "unknown")
            score = match.get("score", 0)
            metadata = match.get("metadata", {})
            values = match.get("values", [])
            
            is_valid, message = check_metadata_fields(metadata)
            
            results.append({
                "vector_id": vector_id,
                "score": score,
                "metadata": metadata,
                "values": values,
                "is_valid": is_valid,
                "validation_message": message
            })
        
        return results
    except Exception as e:
        print(f"Error querying vectors in namespace '{namespace}': {str(e)}")
        raise

def fix_metadata(vector):
    """Fix metadata issues in a vector"""
    metadata = vector["metadata"]
    fixed_metadata = metadata.copy()
    
    # Fix missing fields
    if "text" not in fixed_metadata:
        # Try to extract text from markdown field
        if "markdown" in fixed_metadata:
            fixed_metadata["text"] = fixed_metadata["markdown"]
        else:
            fixed_metadata["text"] = "No content available"
    
    if "title" not in fixed_metadata:
        fixed_metadata["title"] = "Untitled Document"
    
    if "url" not in fixed_metadata:
        # Try to extract URL from other fields
        if "chunk_id" in fixed_metadata and "_" in fixed_metadata["chunk_id"]:
            url_part = fixed_metadata["chunk_id"].split("_")[0]
            fixed_metadata["url"] = f"https://{url_part.replace('_', '.')}"
        else:
            fixed_metadata["url"] = "#"
    
    if "source" not in fixed_metadata:
        # Try to extract source from namespace or other fields
        if "chunk_id" in fixed_metadata and "_" in fixed_metadata["chunk_id"]:
            source_part = fixed_metadata["chunk_id"].split("_")[0]
            fixed_metadata["source"] = source_part
        else:
            fixed_metadata["source"] = "unknown"
    
    return fixed_metadata

def update_vector(vector_id, values, metadata, namespace):
    """Update a vector in Pinecone with fixed metadata"""
    try:
        # Prepare upsert data
        upsert_data = {
            "vectors": [{
                "id": vector_id,
                "values": values,
                "metadata": metadata
            }],
            "namespace": namespace
        }
        
        # Upsert to Pinecone
        response = pinecone_request("vectors/upsert", method="POST", data=upsert_data)
        
        return response.get("upsertedCount", 0) > 0
    except Exception as e:
        print(f"Error updating vector {vector_id}: {str(e)}")
        return False

def fix_vectors_in_namespace(namespace, dry_run=True, batch_size=10):
    """Fix metadata issues in vectors in a specific namespace"""
    print(f"\nChecking vectors in namespace '{namespace}'...")
    
    # Query vectors in the namespace
    vectors = query_vectors_in_namespace(namespace, top_k=100)
    
    if not vectors:
        print(f"No vectors found in namespace '{namespace}'")
        return 0
    
    # Filter invalid vectors
    invalid_vectors = [v for v in vectors if not v["is_valid"]]
    
    print(f"Found {len(invalid_vectors)} vectors with invalid metadata out of {len(vectors)} total vectors")
    
    if dry_run:
        print("DRY RUN: No changes will be made")
        
        # Show examples of fixes
        for i, vector in enumerate(invalid_vectors[:3]):
            print(f"\nExample {i+1}:")
            print(f"Vector ID: {vector['vector_id']}")
            print(f"Issue: {vector['validation_message']}")
            print(f"Original metadata: {json.dumps(vector['metadata'], indent=2)}")
            
            fixed_metadata = fix_metadata(vector)
            print(f"Fixed metadata: {json.dumps(fixed_metadata, indent=2)}")
        
        return len(invalid_vectors)
    
    # Fix invalid vectors
    fixed_count = 0
    for i, vector in enumerate(invalid_vectors):
        print(f"Fixing vector {i+1}/{len(invalid_vectors)}: {vector['vector_id']}")
        
        fixed_metadata = fix_metadata(vector)
        success = update_vector(vector['vector_id'], vector['values'], fixed_metadata, namespace)
        
        if success:
            fixed_count += 1
            print(f"  ✅ Fixed metadata for vector {vector['vector_id']}")
        else:
            print(f"  ❌ Failed to fix metadata for vector {vector['vector_id']}")
        
        # Add a small delay to avoid rate limiting
        if (i + 1) % batch_size == 0:
            print(f"Processed {i+1}/{len(invalid_vectors)} vectors. Pausing briefly...")
            time.sleep(1)
    
    print(f"\nFixed {fixed_count} out of {len(invalid_vectors)} invalid vectors in namespace '{namespace}'")
    return fixed_count

def main():
    parser = argparse.ArgumentParser(description="Fix metadata issues in Pinecone vectors")
    parser.add_argument("--namespace", help="Specific namespace to fix (default: fix all)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be fixed without making changes")
    parser.add_argument("--batch-size", type=int, default=10, help="Number of vectors to process before pausing")
    
    args = parser.parse_args()
    
    try:
        # Get index stats
        index_stats = pinecone_request("describe_index_stats")
        total_vector_count = index_stats.get("total_vector_count", 0)
        dimension = index_stats.get("dimension", "unknown")
        
        print(f"\nPinecone Index Information:")
        print(f"Total vectors: {total_vector_count}")
        print(f"Vector dimension: {dimension}")
        
        # List namespaces
        if args.namespace:
            namespaces = [{"name": args.namespace, "vector_count": "unknown"}]
        else:
            namespaces = list_namespaces()
            
        print(f"\nFound {len(namespaces)} namespaces:")
        for ns in namespaces:
            print(f"- {ns['name']}: {ns['vector_count']} vectors")
        
        # Fix vectors in each namespace
        total_fixed = 0
        for ns in namespaces:
            namespace = ns["name"]
            fixed_count = fix_vectors_in_namespace(namespace, args.dry_run, args.batch_size)
            total_fixed += fixed_count
        
        print("\nSummary:")
        if args.dry_run:
            print(f"DRY RUN: Would fix {total_fixed} vectors across {len(namespaces)} namespaces")
            print("Run without --dry-run to apply these changes")
        else:
            print(f"Fixed {total_fixed} vectors across {len(namespaces)} namespaces")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main()) 