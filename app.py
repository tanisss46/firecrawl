#!/usr/bin/env python
"""
Document search web application.
Searches for documents in the PostgreSQL database.
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from db_utils import search_documents, get_sources, get_source_documents, get_document
import psycopg2
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection parameters
DB_PARAMS = {
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "your-password"),
    "host": os.getenv("POSTGRES_HOST", "your-rds-endpoint.us-west-1.rds.amazonaws.com"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "database": os.getenv("POSTGRES_DATABASE", "docs_db")
}

def get_db_connection():
    """Create a database connection"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        return None

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/test-db-connection')
def test_db_connection():
    """Route to test the database connection"""
    try:
        conn = get_db_connection()
        if conn:
            # Create a cursor
            cur = conn.cursor()
            
            # Execute a simple query
            cur.execute('SELECT 1')
            
            # Get results
            result = cur.fetchone()
            
            # Close cursor and connection
            cur.close()
            conn.close()
            
            return jsonify({
                "success": True,
                "message": "Database connection successful",
                "result": result[0],
                "connection_details": {
                    "host": DB_PARAMS["host"],
                    "database": DB_PARAMS["database"],
                    "user": DB_PARAMS["user"],
                }
            })
        else:
            return jsonify({
                "success": False,
                "message": "Failed to connect to database",
                "connection_details": DB_PARAMS
            })
    except Exception as e:
        logger.error(f"Error testing database connection: {e}")
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}",
            "connection_details": DB_PARAMS
        })

@app.route('/search')
def search():
    """Search page."""
    query = request.args.get('q', '')
    source = request.args.get('source', '')
    
    if not query:
        return redirect(url_for('index'))
    
    if source:
        results = search_documents(query, source)
    else:
        results = search_documents(query)
    
    return render_template('search.html', query=query, results=results, source=source)

@app.route('/source/<source>')
def source(source):
    """Source page."""
    documents = get_source_documents(source)
    return render_template('source.html', source=source, documents=documents)

@app.route('/document/<int:doc_id>')
def document(doc_id):
    """Document page."""
    document = get_document(doc_id)
    if not document:
        return redirect(url_for('index'))
    
    return render_template('document.html', document=document)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create a simple index.html file if it doesn't exist
    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w') as f:
            f.write('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Database Connection Test</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    button {
                        padding: 10px 15px;
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        cursor: pointer;
                    }
                    #result {
                        margin-top: 20px;
                        padding: 20px;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                    }
                </style>
            </head>
            <body>
                <h1>Database Connection Test</h1>
                <button onclick="testConnection()">Test Connection</button>
                <div id="result"></div>
                
                <script>
                    function testConnection() {
                        document.getElementById('result').innerHTML = 'Testing connection...';
                        
                        fetch('/test-db-connection')
                            .then(response => response.json())
                            .then(data => {
                                let resultHtml = '<h2>' + (data.success ? 'Success!' : 'Failed!') + '</h2>';
                                resultHtml += '<p>' + data.message + '</p>';
                                resultHtml += '<h3>Connection Details:</h3>';
                                resultHtml += '<ul>';
                                for (const [key, value] of Object.entries(data.connection_details)) {
                                    resultHtml += '<li><strong>' + key + ':</strong> ' + value + '</li>';
                                }
                                resultHtml += '</ul>';
                                
                                document.getElementById('result').innerHTML = resultHtml;
                            })
                            .catch(error => {
                                document.getElementById('result').innerHTML = '<h2>Error</h2><p>' + error + '</p>';
                            });
                    }
                </script>
            </body>
            </html>
            ''')
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True) 