#!/usr/bin/env python3
"""
Test Pinecone connectivity by directly connecting to the index host
"""

import os
import traceback
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_pinecone_direct():
    """Test Pinecone connectivity by directly connecting to the index host."""
    try:
        # Get API key from environment
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not pinecone_api_key:
            print("PINECONE_API_KEY not found in environment variables.")
            return False
            
        print(f"API Key: {pinecone_api_key[:5]}...{pinecone_api_key[-5:]}")
        
        # Direct connection to the index host from the dashboard
        host = "https://mcp-index-3jg9lch.svc.aped-4627-b74a.pinecone.io"
        
        # Test connection by getting index stats
        print(f"Testing direct connection to {host}...")
        
        headers = {
            "Api-Key": pinecone_api_key,
            "Accept": "application/json"
        }
        
        # Try to get index stats
        stats_url = f"{host}/describe_index_stats"
        print(f"Getting index stats from {stats_url}...")
        
        response = requests.post(stats_url, headers=headers, json={})
        
        if response.status_code == 200:
            print("Successfully connected to Pinecone index!")
            print(f"Index stats: {response.json()}")
            
            # Try a simple upsert
            print("Testing vector upsert...")
            
            # Create a test vector with 1024 dimensions (for multilingual-e5-large)
            upsert_url = f"{host}/vectors/upsert"
            
            upsert_data = {
                "vectors": [{
                    "id": "test-vector-direct",
                    "values": [0.1] * 1024,
                    "metadata": {
                        "text": "This is a test vector for direct connection",
                        "source": "test_pinecone_direct.py"
                    }
                }],
                "namespace": "test-direct"
            }
            
            upsert_response = requests.post(upsert_url, headers=headers, json=upsert_data)
            
            if upsert_response.status_code == 200:
                print("Successfully upserted test vector!")
                print(f"Upsert response: {upsert_response.json()}")
                
                # Try a query
                print("Testing vector query...")
                
                query_url = f"{host}/query"
                query_data = {
                    "vector": [0.1] * 1024,
                    "top_k": 1,
                    "namespace": "test-direct",
                    "include_values": True,
                    "include_metadata": True
                }
                
                query_response = requests.post(query_url, headers=headers, json=query_data)
                
                if query_response.status_code == 200:
                    print("Successfully queried vectors!")
                    print(f"Query response: {query_response.json()}")
                    return True
                else:
                    print(f"Query failed with status code {query_response.status_code}")
                    print(f"Response: {query_response.text}")
                    return False
            else:
                print(f"Upsert failed with status code {upsert_response.status_code}")
                print(f"Response: {upsert_response.text}")
                return False
        else:
            print(f"Connection failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error testing Pinecone direct connection: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing direct Pinecone connectivity...")
    success = test_pinecone_direct()
    print(f"Test completed. Success: {success}") 