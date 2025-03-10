import os
import json
import psycopg2
from psycopg2.extras import Json
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_PARAMS = {
    "user": os.getenv("DB_USER", ""),
    "password": os.getenv("DB_PASSWORD", ""),
    "host": os.getenv("DB_HOST", ""),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "")
}

def get_domain_name(url):
    """Extracts domain name from URL."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain.replace(".", "_")

def get_db_connection():
    """Create a database connection"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def create_tables():
    """Create database tables if they don't exist."""
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database for table creation.")
            return False
        
        cur = conn.cursor()
        
        # Create sources table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS sources (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                base_url VARCHAR(255) NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_crawled_at TIMESTAMP
            )
        ''')
        
        # Create documents table
        cur.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                source_id INTEGER REFERENCES sources(id),
                title VARCHAR(255),
                content TEXT,
                markdown TEXT,
                url VARCHAR(512) NOT NULL,
                crawl_time TIMESTAMP,
                status_code INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                CONSTRAINT unique_url UNIQUE (url)
            )
        ''')
        
        # Create document_metadata table if needed
        cur.execute('''
            CREATE TABLE IF NOT EXISTS document_metadata (
                id SERIAL PRIMARY KEY,
                document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
                key VARCHAR(255) NOT NULL,
                value TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create search_logs table if needed
        cur.execute('''
            CREATE TABLE IF NOT EXISTS search_logs (
                id SERIAL PRIMARY KEY,
                query TEXT NOT NULL,
                results_count INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        print("Database tables created successfully.")
        return True
    except Exception as e:
        print(f"Error creating database tables: {e}")
        return False
    finally:
        if conn:
            conn.close()

def save_to_postgres(results, base_url):
    """Save crawl results to PostgreSQL database."""
    if not results:
        print("No results to save to database.")
        return 0
    
    # Create database tables if they don't exist
    create_tables()
    
    conn = None
    saved_count = 0
    
    try:
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database.")
            return 0
        
        cur = conn.cursor()
        
        # Extract domain for source name
        domain_name = get_domain_name(base_url)
        
        # Check if source exists, if not create it
        cur.execute("SELECT id FROM sources WHERE name = %s", (domain_name,))
        source_row = cur.fetchone()
        
        if source_row:
            source_id = source_row[0]
            print(f"Source '{domain_name}' exists with ID {source_id}.")
        else:
            # Create new source
            cur.execute(
                "INSERT INTO sources (name, base_url, description) VALUES (%s, %s, %s) RETURNING id",
                (domain_name, base_url, f"Documentation for {domain_name}")
            )
            source_id = cur.fetchone()[0]
            print(f"Created new source '{domain_name}' with ID {source_id}.")
        
        # Save each document
        for page in results:
            if "markdown" in page and "metadata" in page and "sourceURL" in page["metadata"]:
                url = page["metadata"]["sourceURL"]
                markdown_content = page["markdown"]
                title = page["metadata"].get("title", url.split("/")[-1])
                status_code = page["metadata"].get("statusCode", 200)
                crawl_time = page["metadata"].get("crawlTime")
                
                # Insert or update document
                try:
                    cur.execute(
                        """
                        INSERT INTO documents (source_id, url, title, content, markdown, status_code, crawl_time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (url) 
                        DO UPDATE SET
                            title = EXCLUDED.title,
                            content = EXCLUDED.content,
                            markdown = EXCLUDED.markdown,
                            status_code = EXCLUDED.status_code,
                            crawl_time = EXCLUDED.crawl_time,
                            updated_at = CURRENT_TIMESTAMP
                        RETURNING id
                        """,
                        (source_id, url, title, markdown_content, markdown_content, status_code, crawl_time)
                    )
                    document_id = cur.fetchone()[0]
                    saved_count += 1
                    
                    # Add metadata as separate entries if needed
                    for key, value in page["metadata"].items():
                        if key not in ["sourceURL", "title", "statusCode", "crawlTime"]:
                            cur.execute(
                                """
                                INSERT INTO document_metadata (document_id, key, value)
                                VALUES (%s, %s, %s)
                                """,
                                (document_id, key, str(value))
                            )
                except Exception as e:
                    print(f"Error saving document {url}: {e}")
                    continue
        
        # Update last_crawled_at in sources table
        cur.execute(
            "UPDATE sources SET last_crawled_at = CURRENT_TIMESTAMP WHERE id = %s",
            (source_id,)
        )
        
        # Commit the transaction
        conn.commit()
        print(f"Successfully saved {saved_count} documents to database.")
        return saved_count
    
    except Exception as e:
        print(f"Error saving to database: {e}")
        if conn:
            conn.rollback()
        return 0
    
    finally:
        if conn:
            conn.close()

def search_documents(query, source=None, limit=20):
    """Search for documents containing the query text."""
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database for search.")
            return []
        
        cur = conn.cursor()
        
        # Build the query
        sql = """
            SELECT id, url, title, 
                   CASE WHEN length(content) <= 300 
                        THEN content 
                        ELSE substring(content, 1, 300) 
                   END as content_preview,
                   source
            FROM documents
            WHERE content ILIKE %s
        """
        params = [f"%{query}%"]
        
        # Add source filter if provided
        if source:
            sql += " AND source = %s"
            params.append(source)
        
        # Add limit
        sql += " ORDER BY updated_at DESC LIMIT %s"
        params.append(limit)
        
        # Execute query
        cur.execute(sql, params)
        results = []
        
        # Process results
        for row in cur.fetchall():
            results.append({
                "id": row[0],
                "url": row[1],
                "title": row[2],
                "content_preview": row[3],
                "source": row[4]
            })
        
        return results
    
    except Exception as e:
        print(f"Error searching documents: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

def get_sources():
    """Get list of all sources with document counts."""
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            print("Failed to connect to database to get sources.")
            return []
        
        cur = conn.cursor()
        cur.execute("SELECT name, base_url, document_count, last_crawled FROM sources ORDER BY name")
        
        sources = []
        for row in cur.fetchall():
            sources.append({
                "name": row[0],
                "base_url": row[1],
                "document_count": row[2],
                "last_crawled": row[3]
            })
        
        return sources
    
    except Exception as e:
        print(f"Error getting sources: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

def get_source_documents(source, limit=100):
    """Get documents for a specific source."""
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            print(f"Failed to connect to database to get documents for source {source}.")
            return []
        
        cur = conn.cursor()
        cur.execute(
            "SELECT id, url, title, updated_at FROM documents WHERE source = %s ORDER BY title LIMIT %s",
            (source, limit)
        )
        
        documents = []
        for row in cur.fetchall():
            documents.append({
                "id": row[0],
                "url": row[1],
                "title": row[2],
                "updated_at": row[3]
            })
        
        return documents
    
    except Exception as e:
        print(f"Error getting documents for source {source}: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

def get_document(doc_id):
    """Get a specific document by ID."""
    conn = None
    try:
        conn = get_db_connection()
        if not conn:
            print(f"Failed to connect to database to get document {doc_id}.")
            return None
        
        cur = conn.cursor()
        cur.execute(
            "SELECT id, url, title, content, source, metadata FROM documents WHERE id = %s",
            (doc_id,)
        )
        
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "url": row[1],
                "title": row[2],
                "content": row[3],
                "source": row[4],
                "metadata": row[5]
            }
        
        return None
    
    except Exception as e:
        print(f"Error getting document {doc_id}: {e}")
        return None
    
    finally:
        if conn:
            conn.close()

# Test database connection if this file is run directly
if __name__ == "__main__":
    print("Testing database connection...")
    conn = get_db_connection()
    if conn:
        print("Database connection successful!")
        conn.close()
    else:
        print("Failed to connect to database.") 