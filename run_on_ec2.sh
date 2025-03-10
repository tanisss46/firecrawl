#!/bin/bash
# Script to run the local documentation crawler and RAG application on an EC2 instance

# Update system packages
echo "Updating system packages..."
sudo apt update -y
sudo apt upgrade -y

# Install Python and pip if not already installed
echo "Installing Python and pip..."
sudo apt install -y python3 python3-pip

# Install required Python packages
echo "Installing required Python packages..."
pip3 install -r requirements.txt

# Install Playwright dependencies
echo "Installing Playwright dependencies..."
python3 -m playwright install --with-deps chromium

# Create log directory
mkdir -p logs

# Run the crawler
echo "Running the documentation crawler..."
python3 local_crawler.py https://docs.vendure.io --limit 50 --max-depth 3 > logs/crawl_$(date +%Y%m%d_%H%M%S).log 2>&1

# Run the RAG application
echo "Starting the RAG application..."
python3 rag_with_docs.py

echo "Done!" 