#!/usr/bin/env python
"""
Document search script.
Searches for documents in the PostgreSQL database.
"""

import sys
import argparse
from db_utils import search_documents, get_sources

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Search for documents in the PostgreSQL database.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--source", help="Search in a specific source")
    parser.add_argument("--limit", type=int, default=10, help="Limit of results")
    args = parser.parse_args()
    
    # If source is specified, search in that source
    if args.source:
        print(f"Searching for '{args.query}' in source '{args.source}'...")
        results = search_documents(args.query, args.source, args.limit)
    else:
        print(f"Searching for '{args.query}' in all sources...")
        results = search_documents(args.query, limit=args.limit)
    
    # Show results
    if not results:
        print("No results found.")
        return
    
    print(f"{len(results)} results found:\n")
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   Source: {result['source']}")
        print(f"   Preview: {result['content_preview']}...")
        print()
    
    # List sources
    print("\nAvailable sources:")
    sources = get_sources()
    for source in sources:
        print(f"- {source['name']}: {source['document_count']} documents")

if __name__ == "__main__":
    main() 