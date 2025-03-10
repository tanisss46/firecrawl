# Local Documentation Crawler

This project demonstrates how to crawl documentation websites locally using Playwright and save the content for further processing.

## Overview

This project provides a Python script that crawls websites using Playwright and converts the content into clean markdown or structured data. This script:

1. Crawls a documentation website to discover all URLs
2. Saves the website content in markdown and JSON formats
3. Provides clean and filtered content

## Requirements

- Python 3.7+
- Playwright

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright:
   ```bash
   python -m playwright install --with-deps chromium
   ```

## Usage

### Basic Usage

Run the script with default settings:

```bash
python local_crawler.py https://docs.vendure.io --limit 50 --max-depth 3
```

This will:
1. Crawl the docs.vendure.io website
2. Crawl a maximum of 50 pages
3. Go down to a maximum depth of 3
4. Save the content to the `docs/` directory

### Customization

You can change the parameters when running the `local_crawler.py` script:

```bash
python local_crawler.py https://your-docs-site.com --limit 100 --max-depth 5
```

### RAG Application

You can run a Retrieval-Augmented Generation (RAG) application using the crawled documentation:

```bash
python rag_with_docs.py
```

This will load the crawled documents and allow you to ask questions about the documentation.

## Output

The script produces the following outputs:

- `docs/`: Main directory
  - `domain_name/`: A directory for each domain (e.g., `docs_vendure_io/`)
    - `crawl_result.json`: Full crawl result
    - `.json` and `.md` files for each crawled page
    - Metadata for each page

## Running on EC2

To run this script on an EC2 instance:

1. Launch an EC2 instance with Amazon Linux 2 or Ubuntu
2. Connect to the instance using SSH
3. Install Python and pip:
   ```bash
   # For Amazon Linux
   sudo yum update -y
   sudo yum install python3 python3-pip -y
   
   # For Ubuntu
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```
4. Copy the script to the EC2 instance
5. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   python3 -m playwright install --with-deps chromium
   ```
6. Run the script:
   ```bash
   ./run_on_ec2.sh
   ```

You can set up a cron job for automated or scheduled crawling:
```bash
crontab -e
# Add a line to run the script every day at 2 AM
0 2 * * * cd /path/to/script && ./run_on_ec2.sh
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 