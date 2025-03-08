#!/usr/bin/env python3
"""
Local Documentation Crawler

This script crawls documentation websites locally using Playwright,
without relying on the Firecrawl API.
"""

import os
import json
import re
import argparse
import urllib.parse
import time
from pathlib import Path
import asyncio
from typing import List, Dict, Any, Optional, Set
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright, Page, Browser, BrowserContext

def clean_markdown_content(markdown_content):
    """Cleans the markdown content."""
    print("Cleaning content...")
    
    # Step 1: Clean header section
    markdown_content = re.sub(r'\[.*? home page.*?\]\(https?://.*?\)', '', markdown_content, flags=re.DOTALL)
    
    # Step 2: Remove simple phrases
    patterns = [
        r'Search\.\.\.',
        r'Ctrl K',
        r'Navigation',
        r'English',
        r'Copy',
        r'Was this page helpful\?',
        r'YesNo',
        r'On this page',
        r'Try in Console',
        r'© \d{4}.*',
    ]
    
    for pattern in patterns:
        markdown_content = re.sub(pattern, '', markdown_content, flags=re.MULTILINE)
    
    # Step 3: Split content into lines and find main content
    lines = markdown_content.split('\n')
    
    # Check first 15 lines and start from the line with meaningful content
    start_index = 0
    for i, line in enumerate(lines[:20]):
        # Find the beginning of meaningful content (usually a heading or paragraph)
        if re.match(r'^#+\s+', line) or (len(line) > 30 and not re.search(r'https?://', line)):
            start_index = i
            break
    
    # If no meaningful content is found, skip the first 15 lines
    if start_index == 0 and len(lines) > 15:
        start_index = 15
    
    # Create new content
    markdown_content = '\n'.join(lines[start_index:])
    
    # Step 4: Empty link text links
    markdown_content = re.sub(r'\[\]\(https?://[^\)]+\)', '', markdown_content)
    
    # Step 5: Clean heading links but keep headings
    markdown_content = re.sub(r'\[​\]\(https?://[^\)]+\)', '', markdown_content)
    
    # Step 6: Clean empty lines and extra spaces
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    markdown_content = re.sub(r' {2,}', ' ', markdown_content)
    
    # Step 7: Clean empty bullet points
    markdown_content = re.sub(r'- \n', '', markdown_content)
    
    # Final cleanup
    markdown_content = markdown_content.strip()
    
    return markdown_content

def get_domain_name(url):
    """Extracts domain name from URL."""
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    return domain.replace(".", "_")

def create_filename(url, domain_name):
    """Creates filename from URL."""
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path.strip("/")
    
    if not path:
        return f"{domain_name}_index"
    
    # Convert URL path to filename
    filename = path.replace("/", "_").replace(".", "_")
    
    # Shorten very long filenames
    if len(filename) > 100:
        filename = filename[:100]
    
    return f"{domain_name}_{filename}"

def is_same_domain(url1, url2):
    """Check if two URLs belong to the same domain."""
    domain1 = urlparse(url1).netloc
    domain2 = urlparse(url2).netloc
    return domain1 == domain2

def is_valid_url(url):
    """Check if URL is valid and not a fragment."""
    if not url:
        return False
    
    parsed = urlparse(url)
    
    # Skip fragment-only URLs
    if not parsed.netloc and not parsed.path and parsed.fragment:
        return False
    
    # Skip mailto, tel, javascript, etc.
    if parsed.scheme and parsed.scheme not in ['http', 'https']:
        return False
    
    return True

async def extract_links(page: Page, base_url: str) -> List[str]:
    """Extract all links from the page."""
    links = await page.evaluate('''() => {
        const anchors = Array.from(document.querySelectorAll('a[href]'));
        return anchors.map(a => a.href);
    }''')
    
    # Filter and normalize links
    valid_links = []
    for link in links:
        if is_valid_url(link) and is_same_domain(link, base_url):
            # Normalize URL (remove fragments)
            parsed = urlparse(link)
            normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if parsed.query:
                normalized += f"?{parsed.query}"
            valid_links.append(normalized)
    
    return list(set(valid_links))  # Remove duplicates

def fix_markdown_line_breaks(markdown_content):
    """
    Markdown içeriğindeki satır sonlarını düzeltir.
    Çok uzun satırları böler ve gereksiz satır sonlarını temizler.
    """
    # Satırları böl
    lines = markdown_content.split('\n')
    
    # Düzeltilmiş satırları tutacak liste
    fixed_lines = []
    
    # Her satırı işle
    for line in lines:
        # Satır sonundaki % karakterlerini temizle
        line = re.sub(r'%+\s*$', '', line)
        
        # Çok uzun satırları böl (80 karakterden uzun olanları)
        if len(line) > 80 and not line.startswith('```') and not line.startswith('#'):
            # Satırı kelimelere böl
            words = line.split()
            
            # Yeni satır oluştur
            new_line = ''
            
            # Her kelimeyi ekle ve satır uzunluğunu kontrol et
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    fixed_lines.append(new_line)
                    new_line = word
                else:
                    if new_line:
                        new_line += ' ' + word
                    else:
                        new_line = word
            
            # Son satırı ekle
            if new_line:
                fixed_lines.append(new_line)
        else:
            fixed_lines.append(line)
    
    # Satırları birleştir
    fixed_markdown = '\n'.join(fixed_lines)
    
    # Gereksiz boş satırları temizle
    fixed_markdown = re.sub(r'\n{3,}', '\n\n', fixed_markdown)
    
    # Sondaki gereksiz karakterleri temizle
    fixed_markdown = fixed_markdown.rstrip('%\n\t ')
    
    return fixed_markdown

async def html_to_markdown(page: Page) -> str:
    """Convert HTML to Markdown using Playwright."""
    # Extract content as markdown with images in their original positions
    markdown = await page.evaluate(r'''() => {
        function getTextContent(element, depth = 0) {
            let text = '';
            
            // Skip hidden elements
            if (window.getComputedStyle(element).display === 'none' || 
                window.getComputedStyle(element).visibility === 'hidden') {
                return '';
            }
            
            // Skip navigation, footer, etc.
            const skipTags = ['nav', 'footer', 'header', 'aside'];
            if (skipTags.includes(element.tagName.toLowerCase())) {
                return '';
            }
            
            // Skip elements with certain classes or roles
            const skipClasses = ['nav', 'footer', 'header', 'sidebar', 'menu', 'toc', 'breadcrumb'];
            const skipRoles = ['navigation', 'complementary'];
            
            // Check if element.className is a string before using includes
            if (element.className && typeof element.className === 'string') {
                for (const cls of skipClasses) {
                    if (element.className.indexOf(cls) !== -1) {
                        return '';
                    }
                }
            }
            
            if (element.getAttribute('role') && skipRoles.includes(element.getAttribute('role'))) {
                return '';
            }
            
            // Process headings
            if (element.tagName.match(/^H[1-6]$/)) {
                const level = element.tagName[1];
                const hashes = '#'.repeat(parseInt(level));
                return "\n" + hashes + " " + element.textContent.trim() + "\n\n";
            }
            
            // Process images directly
            if (element.tagName === 'IMG') {
                const src = element.getAttribute('src');
                const alt = element.getAttribute('alt') || '';
                
                // Skip tiny images, icons, and logos
                if (element.width < 100 && element.height < 100) {
                    return '';
                }
                
                // Skip if no src
                if (!src) {
                    return '';
                }
                
                // Convert relative URLs to absolute
                let absoluteSrc = src;
                if (src.startsWith('/')) {
                    absoluteSrc = window.location.origin + src;
                }
                
                return `\n\n![${alt}](${absoluteSrc})\n\n`;
            }
            
            // Process paragraphs
            if (element.tagName === 'P') {
                let paragraphText = element.textContent.trim();
                
                // Check if paragraph has any images
                const images = element.querySelectorAll('img');
                if (images.length > 0) {
                    let imageMarkdown = '';
                    
                    for (const img of images) {
                        // Skip tiny images, icons, and logos
                        if (img.width < 100 && img.height < 100) {
                            continue;
                        }
                        
                        const src = img.getAttribute('src');
                        const alt = img.getAttribute('alt') || '';
                        
                        // Skip if no src
                        if (!src) {
                            continue;
                        }
                        
                        // Convert relative URLs to absolute
                        let absoluteSrc = src;
                        if (src.startsWith('/')) {
                            absoluteSrc = window.location.origin + src;
                        }
                        
                        imageMarkdown += `\n\n![${alt}](${absoluteSrc})\n\n`;
                    }
                    
                    return "\n" + paragraphText + "\n\n" + imageMarkdown;
                }
                
                return "\n" + paragraphText + "\n\n";
            }
            
            // Process lists
            if (element.tagName === 'LI') {
                return "- " + element.textContent.trim() + "\n";
            }
            
            // Process links
            if (element.tagName === 'A' && element.href) {
                // Convert relative URLs to absolute
                let href = element.href;
                if (href.startsWith('/')) {
                    href = window.location.origin + href;
                }
                return "[" + element.textContent.trim() + "](" + href + ")";
            }
            
            // Process code blocks
            if (element.tagName === 'PRE' || element.tagName === 'CODE') {
                return "\n```\n" + element.textContent + "\n```\n\n";
            }
            
            // Process figure elements with images
            if (element.tagName === 'FIGURE') {
                const img = element.querySelector('img');
                const figcaption = element.querySelector('figcaption');
                
                if (img) {
                    const src = img.getAttribute('src');
                    let alt = img.getAttribute('alt') || '';
                    
                    // Use figcaption as alt text if available
                    if (figcaption && figcaption.textContent) {
                        alt = figcaption.textContent.trim();
                    }
                    
                    // Skip if no src
                    if (!src) {
                        return '';
                    }
                    
                    // Convert relative URLs to absolute
                    let absoluteSrc = src;
                    if (src.startsWith('/')) {
                        absoluteSrc = window.location.origin + src;
                    }
                    
                    return `\n\n![${alt}](${absoluteSrc})\n\n`;
                }
            }
            
            // Process div elements that might contain images
            if (element.tagName === 'DIV') {
                // First get text from all child text nodes
                let divText = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.TEXT_NODE) {
                        divText += child.textContent;
                    }
                }
                
                // Then process all child elements
                let childContent = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.ELEMENT_NODE) {
                        childContent += getTextContent(child, depth + 1);
                    }
                }
                
                // If this div has direct text content, format it as a paragraph
                if (divText.trim()) {
                    return "\n" + divText.trim() + "\n\n" + childContent;
                }
                
                return childContent;
            }
            
            // Process children for other elements
            for (const child of element.childNodes) {
                if (child.nodeType === Node.TEXT_NODE) {
                    text += child.textContent;
                } else if (child.nodeType === Node.ELEMENT_NODE) {
                    text += getTextContent(child, depth + 1);
                }
            }
            
            return text;
        }
        
        // Start with the main content if available
        const mainContent = document.querySelector('main') || 
                           document.querySelector('[role="main"]') || 
                           document.querySelector('.content') || 
                           document.querySelector('article') || 
                           document.body;
        
        // Get content with images in their original positions
        let content = getTextContent(mainContent);
        
        // Extract all links for a separate section
        const links = mainContent.querySelectorAll('a[href]');
        let linksMarkdown = '\n\n## Links\n\n';
        let addedLinks = new Set();
        
        for (const link of links) {
            const href = link.getAttribute('href');
            const text = link.textContent.trim();
            
            // Skip empty links, fragment links, and non-http links
            if (!href || href.startsWith('#') || (!href.startsWith('http') && !href.startsWith('/'))) {
                continue;
            }
            
            // Skip navigation links
            if (link.closest('nav') || link.closest('header') || link.closest('footer')) {
                continue;
            }
            
            // Convert relative URLs to absolute
            let absoluteHref = href;
            if (href.startsWith('/')) {
                absoluteHref = window.location.origin + href;
            }
            
            // Skip if already added
            if (addedLinks.has(absoluteHref)) {
                continue;
            }
            
            addedLinks.add(absoluteHref);
            linksMarkdown += `- [${text}](${absoluteHref})\n`;
        }
        
        return content + (addedLinks.size > 0 ? linksMarkdown : '');
    }''')
    
    # JavaScript'ten dönen metindeki tüm \n karakterlerini gerçek satır sonlarına dönüştür
    markdown = markdown.replace('\\n', '\n')
    
    # Eğer hala \n karakterleri varsa, bunları da dönüştür (regex kullanarak)
    markdown = re.sub(r'\\n', '\n', markdown)
    
    # Markdown içeriğindeki satır sonlarını düzelt
    markdown = fix_markdown_line_breaks(markdown)
    
    # Tekrarlanan resim bağlantılarını temizle
    markdown = re.sub(r'(!\[.*?\]\(.*?\))\s*\1', r'\1', markdown)
    
    return markdown

async def crawl_page(page: Page, url: str) -> Dict[str, Any]:
    """Crawl a single page and extract its content."""
    print(f"Crawling: {url}")
    
    try:
        # Navigate to the page
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Wait for content to load
        await page.wait_for_load_state("domcontentloaded")
        
        # Extract metadata
        title = await page.title()
        
        # Extract description
        description = await page.evaluate('''() => {
            const meta = document.querySelector('meta[name="description"]') || 
                         document.querySelector('meta[property="og:description"]');
            return meta ? meta.getAttribute('content') : '';
        }''')
        
        # Convert HTML to Markdown
        markdown = await html_to_markdown(page)
        
        # Clean markdown content
        cleaned_markdown = clean_markdown_content(markdown)
        
        # Extract links for further crawling
        links = await extract_links(page, url)
        
        return {
            "markdown": cleaned_markdown,
            "metadata": {
                "title": title,
                "description": description,
                "sourceURL": url
            },
            "links": links
        }
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")
        return {
            "markdown": "",
            "metadata": {
                "title": "",
                "description": "",
                "sourceURL": url,
                "error": str(e)
            },
            "links": []
        }

async def crawl_website(url: str, limit: int = 10, max_depth: int = 3) -> List[Dict[str, Any]]:
    """Crawl a website starting from the given URL."""
    results = []
    visited_urls = set()
    urls_to_visit = [(url, 0)]  # (url, depth)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        
        # Block ads and media to speed up crawling
        await context.route('**/*.{png,jpg,jpeg,gif,svg,mp3,mp4,avi,flac,ogg,wav,webm}', lambda route: route.abort())
        await context.route('**/ads/**', lambda route: route.abort())
        
        page = await context.new_page()
        
        while urls_to_visit and len(visited_urls) < limit:
            current_url, depth = urls_to_visit.pop(0)
            
            if current_url in visited_urls:
                continue
                
            visited_urls.add(current_url)
            
            result = await crawl_page(page, current_url)
            results.append(result)
            
            print(f"Crawled {len(visited_urls)}/{limit} pages. Current depth: {depth}")
            
            # Add new URLs to visit if we haven't reached max depth
            if depth < max_depth:
                new_links = result.get("links", [])
                for link in new_links:
                    if link not in visited_urls and len(visited_urls) + len(urls_to_visit) < limit:
                        urls_to_visit.append((link, depth + 1))
        
        await browser.close()
    
    return results

def save_crawl_results(results, base_url):
    """Saves crawl results to files."""
    if not results:
        print("No data to save!")
        return
    
    # Create docs directory
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    
    # Get domain name
    domain_name = get_domain_name(base_url)
    
    # Create directory for domain
    domain_dir = docs_dir / domain_name
    domain_dir.mkdir(exist_ok=True)
    
    # Save each page
    for page in results:
        if "markdown" in page and "metadata" in page and "sourceURL" in page["metadata"]:
            url = page["metadata"]["sourceURL"]
            markdown_content = page["markdown"]
            
            # Create filename
            filename = create_filename(url, domain_name)
            
            # Save JSON file
            json_path = domain_dir / f"{filename}.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump({
                    "content": markdown_content,
                    "metadata": page["metadata"]
                }, f, ensure_ascii=False, indent=2)
            
            # Save Markdown file
            md_path = domain_dir / f"{filename}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            
            print(f"Saved files: {filename}.json, {filename}.md")
    
    # Save full crawl result
    crawl_result_path = domain_dir / "crawl_result.json"
    with open(crawl_result_path, "w", encoding="utf-8") as f:
        json.dump({
            "data": results,
            "totalCount": len(results)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"All files saved to '{domain_dir}' directory.")
    print(f"Full crawl result saved to '{crawl_result_path}'")

async def main_async():
    """Async main function."""
    parser = argparse.ArgumentParser(description="Crawl websites locally using Playwright.")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of pages to crawl (default: 10)")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth to crawl (default: 3)")
    
    args = parser.parse_args()
    
    print(f"Starting local crawl for: {args.url}")
    print(f"Limit: {args.limit}, Max Depth: {args.max_depth}")
    
    start_time = time.time()
    
    # Crawl website
    results = await crawl_website(args.url, args.limit, args.max_depth)
    
    # Save results
    save_crawl_results(results, args.url)
    
    end_time = time.time()
    print(f"Crawl completed in {end_time - start_time:.2f} seconds.")
    print(f"Total pages crawled: {len(results)}")

def main():
    """Main function."""
    asyncio.run(main_async())

if __name__ == "__main__":
    main() 