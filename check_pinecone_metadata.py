#!/usr/bin/env python3
"""
Check if vectors in Pinecone have been saved with the correct metadata.
This script will:
1. Connect to Pinecone
2. List available namespaces
3. Query vectors from each namespace
4. Check if the metadata fields are present and correctly formatted
"""

import os
import requests
import json
import argparse
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

def query_vectors_in_namespace(namespace, top_k=5):
    """Query vectors in a specific namespace and check their metadata"""
    try:
        # Use a simple query vector (all zeros)
        query_vector = [0.0] * 1024  # Assuming 1024-dimensional vectors
        
        # Query Pinecone
        data = {
            "vector": query_vector,
            "topK": top_k,
            "includeMetadata": True,
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
            
            is_valid, message = check_metadata_fields(metadata)
            
            results.append({
                "vector_id": vector_id,
                "score": score,
                "metadata": metadata,
                "is_valid": is_valid,
                "validation_message": message
            })
        
        return results
    except Exception as e:
        print(f"Error querying vectors in namespace '{namespace}': {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Check if vectors in Pinecone have correct metadata")
    parser.add_argument("--namespace", help="Specific namespace to check (default: check all)")
    parser.add_argument("--top-k", type=int, default=5, help="Number of vectors to check per namespace")
    parser.add_argument("--verbose", action="store_true", help="Show detailed metadata for each vector")
    
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
        
        # Check vectors in each namespace
        all_valid = True
        for ns in namespaces:
            namespace = ns["name"]
            print(f"\nChecking vectors in namespace '{namespace}'...")
            
            results = query_vectors_in_namespace(namespace, args.top_k)
            
            if not results:
                continue
                
            valid_count = sum(1 for r in results if r["is_valid"])
            print(f"Checked {len(results)} vectors, {valid_count} have valid metadata")
            
            for i, result in enumerate(results):
                if not result["is_valid"]:
                    all_valid = False
                    print(f"  Vector {result['vector_id']}: INVALID - {result['validation_message']}")
                elif args.verbose:
                    print(f"  Vector {result['vector_id']}: VALID")
                
                if args.verbose:
                    print(f"    Metadata: {json.dumps(result['metadata'], indent=2)}")
        
        print("\nSummary:")
        if all_valid:
            print("✅ All checked vectors have valid metadata")
        else:
            print("❌ Some vectors have invalid or missing metadata")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main()) 