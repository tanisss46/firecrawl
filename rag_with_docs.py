#!/usr/bin/env python3
"""
RAG with Documentation

This script demonstrates how to use the crawled documentation for a
Retrieval-Augmented Generation (RAG) application.
"""

import os
import json
import glob
from typing import List, Dict, Any
from pathlib import Path

# You would typically use a proper vector database and embedding model
# This is a simplified example using basic text search
def simple_search(query: str, documents: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
    """
    Simple search function to find relevant documents based on keyword matching.
    
    Args:
        query (str): The search query.
        documents (List[Dict]): List of documents to search through.
        top_k (int): Number of top results to return.
    
    Returns:
        List[Dict]: Top matching documents.
    """
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Calculate a simple relevance score based on word matching
    scored_docs = []
    for doc in documents:
        if "content" in doc:
            content = doc["content"].lower()
        elif "markdown" in doc:
            content = doc["markdown"].lower()
        else:
            continue
        
        score = 0
        
        # Count occurrences of query words in the document
        for word in query_lower.split():
            if len(word) > 3:  # Ignore short words
                score += content.count(word)
        
        # Add document with its score if there's any match
        if score > 0:
            scored_docs.append({"document": doc, "score": score})
    
    # Sort by score in descending order and take top_k
    scored_docs.sort(key=lambda x: x["score"], reverse=True)
    return [item["document"] for item in scored_docs[:top_k]]

def load_crawled_documents(crawl_result_path: str) -> List[Dict[str, Any]]:
    """
    Load documents from a crawl result file.
    
    Args:
        crawl_result_path (str): Path to the crawl_result.json file.
    
    Returns:
        List[Dict]: List of documents.
    """
    try:
        with open(crawl_result_path, 'r', encoding='utf-8') as f:
            crawl_result = json.load(f)
        
        if "data" in crawl_result:
            return crawl_result["data"]
        else:
            print(f"No 'data' field found in {crawl_result_path}")
            return []
    except Exception as e:
        print(f"Error loading crawl result: {e}")
        return []

def load_individual_documents(docs_dir: str) -> List[Dict[str, Any]]:
    """
    Load individual markdown documents from a directory.
    
    Args:
        docs_dir (str): Directory containing markdown files.
    
    Returns:
        List[Dict]: List of documents.
    """
    documents = []
    
    # Find all JSON files (they contain both content and metadata)
    json_files = glob.glob(os.path.join(docs_dir, "**/*.json"), recursive=True)
    
    # Filter out crawl_result.json
    json_files = [f for f in json_files if not f.endswith("crawl_result.json")]
    
    for json_file in json_files:
        try:
            # Read JSON content
            with open(json_file, 'r', encoding='utf-8') as f:
                doc_data = json.load(f)
            
            documents.append(doc_data)
        except Exception as e:
            print(f"Error loading document {json_file}: {e}")
    
    return documents

def generate_answer(query: str, relevant_docs: List[Dict[str, Any]]) -> str:
    """
    Generate an answer based on the query and relevant documents.
    
    In a real application, you would use an LLM API here.
    This is a simplified example that just concatenates information.
    
    Args:
        query (str): The user's query.
        relevant_docs (List[Dict]): Relevant documents for the query.
    
    Returns:
        str: Generated answer.
    """
    # In a real application, you would call an LLM API here
    # For example:
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided documentation."},
    #         {"role": "user", "content": f"Question: {query}\n\nRelevant documentation:\n{relevant_docs_text}"}
    #     ]
    # )
    # return response.choices[0].message.content
    
    # Simplified example:
    if not relevant_docs:
        return "I couldn't find any relevant information to answer your question."
    
    # Extract titles and snippets from relevant documents
    answer_parts = ["Here's what I found in the documentation:"]
    
    for i, doc in enumerate(relevant_docs, 1):
        # Handle different document formats
        if "metadata" in doc:
            title = doc.get("metadata", {}).get("title", f"Document {i}")
            url = doc.get("metadata", {}).get("sourceURL", "")
        else:
            title = f"Document {i}"
            url = ""
        
        # Extract content based on document format
        if "content" in doc:
            content = doc["content"]
        elif "markdown" in doc:
            content = doc["markdown"]
        else:
            content = "No content available"
        
        # Extract a relevant snippet (first 200 characters for simplicity)
        snippet = content[:200] + "..." if len(content) > 200 else content
        
        answer_parts.append(f"\n\n## {title}")
        answer_parts.append(snippet)
        if url:
            answer_parts.append(f"\nSource: {url}")
    
    return "\n".join(answer_parts)

def find_crawl_results() -> List[str]:
    """
    Find all crawl_result.json files in the docs directory.
    
    Returns:
        List[str]: List of paths to crawl_result.json files.
    """
    docs_dir = Path("docs")
    if not docs_dir.exists():
        return []
    
    return glob.glob(str(docs_dir / "**" / "crawl_result.json"), recursive=True)

def main():
    """Main function to demonstrate RAG with documentation."""
    # Find all crawl results
    crawl_results = find_crawl_results()
    
    if not crawl_results:
        print("No crawl results found. Please run local_crawler.py first.")
        print("Example: python local_crawler.py https://docs.example.com --limit 20")
        return
    
    # Load documents from all crawl results
    all_documents = []
    for crawl_result in crawl_results:
        documents = load_crawled_documents(crawl_result)
        all_documents.extend(documents)
    
    # If no documents found in crawl results, try loading individual files
    if not all_documents:
        all_documents = load_individual_documents("docs")
    
    if not all_documents:
        print("No documents found. Please run local_crawler.py first.")
        return
    
    print(f"Loaded {len(all_documents)} documents from {len(crawl_results)} crawl results.")
    
    # Interactive query loop
    print("\nDocumentation Q&A System")
    print("Type 'exit' to quit.")
    
    while True:
        query = input("\nEnter your question: ")
        if query.lower() in ["exit", "quit", "q"]:
            break
        
        # Find relevant documents
        relevant_docs = simple_search(query, all_documents)
        
        # Generate answer
        answer = generate_answer(query, relevant_docs)
        
        # Print answer
        print("\n" + "=" * 80)
        print(answer)
        print("=" * 80)

if __name__ == "__main__":
    main() 