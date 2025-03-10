#!/usr/bin/env python3
"""
Test Pinecone connectivity using the latest SDK approach
"""

import os
import traceback
from dotenv import load_dotenv
import pinecone

# Load environment variables
load_dotenv()

def test_pinecone():
    """Test Pinecone connectivity using the latest SDK."""
    try:
        # Get API key from environment
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not pinecone_api_key:
            print("PINECONE_API_KEY not found in environment variables.")
            return False
            
        print(f"API Key: {pinecone_api_key[:5]}...{pinecone_api_key[-5:]}")
        
        # Initialize Pinecone with new API format
        print("Initializing Pinecone client...")
        pinecone.init(api_key=pinecone_api_key, environment="us-east-1")
        
        # List available indexes
        print("Listing indexes...")
        indexes = pinecone.list_indexes()
        print(f"Available indexes: {indexes}")
        
        # Connect to the index
        index_name = "mcp-index"
        
        # Check if index exists
        if index_name in indexes:
            print(f"Found index: {index_name}")
        else:
            print(f"Index '{index_name}' not found in the list of indexes.")
            return False
            
        # Connect to the index
        print(f"Connecting to index {index_name}...")
        index = pinecone.Index(index_name)
        print(f"Successfully connected to index: {index_name}")
        
        # Get index stats
        print("Getting index stats...")
        stats = index.describe_index_stats()
        print(f"Index stats: {stats}")
        
        # Test a simple upsert with the correct dimension (1024 for multilingual-e5-large)
        test_vector = [{
            "id": "test-vector-1",
            "values": [0.1] * 1024,  # Using 1024 dimensions
            "metadata": {"test": "data", "text": "Sample text for testing"}
        }]
        
        # Try upserting the test vector
        try:
            print("Upserting test vector...")
            index.upsert(vectors=test_vector, namespace="test-namespace")
            print("Successfully upserted test vector")
            
            # Verify the vector was added
            print("Getting updated index stats...")
            stats_after = index.describe_index_stats()
            print(f"Index stats after upsert: {stats_after}")
            
            # Query the vector
            print("Querying the vector...")
            query_response = index.query(
                namespace="test-namespace",
                vector=[0.1] * 1024,
                top_k=1,
                include_values=True,
                include_metadata=True
            )
            print(f"Query response: {query_response}")
            
            return True
        except Exception as e:
            print(f"Error during upsert/query test: {e}")
            traceback.print_exc()
            return False
            
    except Exception as e:
        print(f"Error testing Pinecone: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Pinecone connectivity...")
    success = test_pinecone()
    print(f"Test completed. Success: {success}") 