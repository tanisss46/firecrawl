import os
import psycopg2
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def init_db():
    """Create database tables."""
    # Local PostgreSQL connection
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "docs_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        port=os.getenv("DB_PORT", 5432)
    )
    conn.autocommit = True
    cur = conn.cursor()
    
    # documents table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        url TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        source TEXT NOT NULL,
        metadata JSONB,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # sources table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sources (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        base_url TEXT NOT NULL,
        description TEXT,
        last_crawled TIMESTAMP,
        document_count INTEGER DEFAULT 0
    )
    """)
    
    # Indexes
    cur.execute("CREATE INDEX IF NOT EXISTS idx_documents_source ON documents(source)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_documents_url ON documents(url)")
    
    cur.close()
    conn.close()
    
    print("Database tables created successfully")

if __name__ == "__main__":
    init_db() 