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
import aiohttp
import requests
from pathlib import Path
import asyncio
from typing import List, Dict, Any, Optional, Set
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
from dotenv import load_dotenv

# Import for PostgreSQL integration
from db_utils import save_to_postgres, get_domain_name, create_tables

# Load environment variables
load_dotenv()

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
    
    # Handle subdomains (e.g., docs.example.com and example.com)
    if domain1.endswith(domain2) or domain2.endswith(domain1):
        return True
    
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
    
    # Skip common file types that aren't documentation
    if parsed.path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.pdf', '.zip', '.tar.gz')):
        return False
    
    return True

def is_docs_url(url, base_url):
    """Check if URL is likely a documentation page."""
    # If it's not the same domain, it's not a docs page
    if not is_same_domain(url, base_url):
        return False
    
    parsed_url = urlparse(url)
    parsed_base = urlparse(base_url)
    
    # If the base URL has a path (like /docs), make sure the URL contains it
    if parsed_base.path and parsed_base.path != '/':
        return parsed_url.path.startswith(parsed_base.path)
    
    return True

async def get_urls_from_sitemap(base_url: str) -> List[str]:
    """Try to get URLs from sitemap.xml."""
    sitemap_urls = []
    possible_sitemaps = [
        f"{base_url}/sitemap.xml",
        f"{base_url}/sitemap_index.xml",
        f"{base_url}/sitemap",
        # Add more common sitemap paths if needed
    ]
    
    # If base_url ends with /, remove it for the next patterns
    base_without_slash = base_url.rstrip('/')
    possible_sitemaps.extend([
        f"{base_without_slash}/sitemap.xml",
        f"{base_without_slash}/sitemap_index.xml",
        f"{base_without_slash}/sitemap",
    ])
    
    # Try to find the sitemap
    async with aiohttp.ClientSession() as session:
        for sitemap_url in possible_sitemaps:
            try:
                print(f"Checking sitemap at: {sitemap_url}")
                async with session.get(sitemap_url, timeout=30) as response:
                    if response.status == 200:
                        content = await response.text()
                        
                        # Check if it's a sitemap index
                        if "<sitemapindex" in content:
                            # Extract sitemap URLs from the index
                            sitemap_matches = re.findall(r'<loc>(.*?)</loc>', content)
                            for sitemap in sitemap_matches:
                                try:
                                    async with session.get(sitemap, timeout=30) as sub_response:
                                        if sub_response.status == 200:
                                            sub_content = await sub_response.text()
                                            # Extract URLs from this sitemap
                                            url_matches = re.findall(r'<loc>(.*?)</loc>', sub_content)
                                            for url in url_matches:
                                                if is_valid_url(url) and is_docs_url(url, base_url):
                                                    sitemap_urls.append(url)
                                except Exception as e:
                                    print(f"Error fetching sub-sitemap {sitemap}: {str(e)}")
                        else:
                            # It's a regular sitemap, extract URLs directly
                            url_matches = re.findall(r'<loc>(.*?)</loc>', content)
                            for url in url_matches:
                                if is_valid_url(url) and is_docs_url(url, base_url):
                                    sitemap_urls.append(url)
                        
                        # If we found URLs, no need to check other possible sitemap locations
                        if sitemap_urls:
                            break
            except Exception as e:
                print(f"Error checking sitemap at {sitemap_url}: {str(e)}")
    
    return sitemap_urls

async def extract_links(page: Page, base_url: str) -> List[str]:
    """Extract all links from the page."""
    links = await page.evaluate('''() => {
        try {
            // Get all links, including those in shadow DOM if possible
            const getAllLinks = (root) => {
                let links = [];
                
                // Get regular links
                const anchors = root.querySelectorAll('a[href]');
                for (const a of anchors) {
                    links.push(a.href);
                }
                
                // Try to get links from shadow roots
                const elementsWithShadow = root.querySelectorAll('*');
                for (const el of elementsWithShadow) {
                    if (el.shadowRoot) {
                        links = links.concat(getAllLinks(el.shadowRoot));
                    }
                }
                
                return links;
            };
            
            return getAllLinks(document);
        } catch (e) {
            console.error("Error extracting links:", e);
            // Fallback to simpler method
            return Array.from(document.querySelectorAll('a[href]')).map(a => a.href);
        }
    }''')
    
    # Filter and normalize links
    valid_links = []
    for link in links:
        if is_valid_url(link) and is_docs_url(link, base_url):
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
                
                // Process links inside headings
                let headingContent = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.TEXT_NODE) {
                        headingContent += child.textContent;
                    } else if (child.nodeType === Node.ELEMENT_NODE) {
                        if (child.tagName === 'A' && child.href) {
                            // Convert relative URLs to absolute
                            let href = child.href;
                            if (href.startsWith('/')) {
                                href = window.location.origin + href;
                            }
                            headingContent += `[${child.textContent.trim()}](${href})`;
                        } else {
                            headingContent += getTextContent(child, depth + 1);
                        }
                    }
                }
                
                return "\n" + hashes + " " + headingContent.trim() + "\n\n";
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
                // Process paragraph content with links and other elements
                let paragraphContent = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.TEXT_NODE) {
                        paragraphContent += child.textContent;
                    } else if (child.nodeType === Node.ELEMENT_NODE) {
                        if (child.tagName === 'A' && child.href) {
                            // Convert relative URLs to absolute
                            let href = child.href;
                            if (href.startsWith('/')) {
                                href = window.location.origin + href;
                            }
                            paragraphContent += `[${child.textContent.trim()}](${href})`;
                        } else if (child.tagName === 'CODE') {
                            paragraphContent += '`' + child.textContent + '`';
                        } else if (child.tagName === 'STRONG' || child.tagName === 'B') {
                            paragraphContent += '**' + child.textContent + '**';
                        } else if (child.tagName === 'EM' || child.tagName === 'I') {
                            paragraphContent += '*' + child.textContent + '*';
                        } else {
                            paragraphContent += getTextContent(child, depth + 1);
                        }
                    }
                }
                
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
                    
                    return "\n" + paragraphContent.trim() + "\n\n" + imageMarkdown;
                }
                
                return "\n" + paragraphContent.trim() + "\n\n";
            }
            
            // Process lists
            if (element.tagName === 'LI') {
                // Process list item content with links and other elements
                let listItemContent = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.TEXT_NODE) {
                        listItemContent += child.textContent;
                    } else if (child.nodeType === Node.ELEMENT_NODE) {
                        if (child.tagName === 'A' && child.href) {
                            // Convert relative URLs to absolute
                            let href = child.href;
                            if (href.startsWith('/')) {
                                href = window.location.origin + href;
                            }
                            listItemContent += `[${child.textContent.trim()}](${href})`;
                        } else if (child.tagName === 'CODE') {
                            listItemContent += '`' + child.textContent + '`';
                        } else if (child.tagName === 'STRONG' || child.tagName === 'B') {
                            listItemContent += '**' + child.textContent + '**';
                        } else if (child.tagName === 'EM' || child.tagName === 'I') {
                            listItemContent += '*' + child.textContent + '*';
                        } else {
                            listItemContent += getTextContent(child, depth + 1);
                        }
                    }
                }
                return "- " + listItemContent.trim() + "\n";
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
            if (element.tagName === 'PRE') {
                const codeElement = element.querySelector('code');
                if (codeElement) {
                    // Try to detect language from class
                    let language = '';
                    if (codeElement.className) {
                        const match = codeElement.className.match(/language-(\w+)/);
                        if (match) {
                            language = match[1];
                        }
                    }
                    return `\n\`\`\`${language}\n${codeElement.textContent}\n\`\`\`\n\n`;
                }
                return "\n```\n" + element.textContent + "\n```\n\n";
            }
            
            // Process inline code
            if (element.tagName === 'CODE') {
                return "`" + element.textContent + "`";
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
                // Process div content with links and other elements
                let divContent = '';
                for (const child of element.childNodes) {
                    if (child.nodeType === Node.TEXT_NODE) {
                        divContent += child.textContent;
                    } else if (child.nodeType === Node.ELEMENT_NODE) {
                        divContent += getTextContent(child, depth + 1);
                    }
                }
                
                // If this div has direct text content, format it as a paragraph
                if (divContent.trim()) {
                    return divContent;
                }
                
                return '';
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
        # Step 1: Navigate to the page with domcontentloaded first (faster)
        await page.goto(url, wait_until="domcontentloaded", timeout=120000)
        
        # Step 2: Try to wait for main content to be visible
        try:
            await page.wait_for_selector(
                "main, article, .content, [role='main'], .documentation, .docs-content, .markdown-body", 
                timeout=20000, 
                state="visible"
            )
        except Exception as e:
            print(f"Main content not immediately visible: {str(e)}")
            # If main content isn't visible yet, try waiting for networkidle
            try:
                await page.wait_for_load_state("networkidle", timeout=30000)
            except Exception as e2:
                print(f"Network not idle: {str(e2)}")
                # If networkidle times out, that's okay, we'll work with what we have
                pass
        
        # Step 3: Additional wait for JavaScript frameworks to render content
        await asyncio.sleep(2)
        
        print(f"Extracting content from: {url}")
        
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
        print(f"Found {len(links)} links on {url}")
        
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

async def crawl_website(url: str, limit: int = 5000, max_depth: int = 10) -> List[Dict[str, Any]]:
    """Crawl a website starting from the given URL."""
    results = []
    visited_urls = set()
    urls_to_visit = [(url, 0)]  # (url, depth)
    
    # Try to get URLs from sitemap first
    print("Checking for sitemap...")
    sitemap_urls = await get_urls_from_sitemap(url)
    if sitemap_urls:
        print(f"Found {len(sitemap_urls)} URLs from sitemap")
        # Add sitemap URLs to the queue with priority
        for sitemap_url in sitemap_urls:
            if sitemap_url not in visited_urls and sitemap_url not in [u for u, _ in urls_to_visit]:
                # Add with depth 1 to prioritize these URLs
                urls_to_visit.append((sitemap_url, 1))
    
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
        page.set_default_timeout(120000)  # Set default timeout to 120 seconds
        
        try:
            while urls_to_visit and len(visited_urls) < limit:
                current_url, depth = urls_to_visit.pop(0)
                
                if current_url in visited_urls:
                    continue
                    
                visited_urls.add(current_url)
                
                try:
                    # Try to crawl with retry mechanism
                    max_retries = 2
                    result = None
                    
                    for retry in range(max_retries + 1):
                        try:
                            result = await crawl_page(page, current_url)
                            break  # Success, exit retry loop
                        except Exception as retry_error:
                            if retry < max_retries:
                                print(f"Attempt {retry+1} failed for {current_url}: {str(retry_error)}. Retrying...")
                                await asyncio.sleep(5)  # Wait before retry
                            else:
                                print(f"All {max_retries+1} attempts failed for {current_url}")
                                # Create an empty result for failed pages
                                result = {
                                    "markdown": "",
                                    "metadata": {
                                        "title": "",
                                        "description": "",
                                        "sourceURL": current_url,
                                        "error": str(retry_error)
                                    },
                                    "links": []
                                }
                    
                    # Add the result (either successful or empty)
                    results.append(result)
                    
                    print(f"Crawled {len(visited_urls)}/{limit} pages. Current depth: {depth}")
                    
                    # Add new URLs to visit if we haven't reached max depth
                    if depth < max_depth:
                        new_links = result.get("links", [])
                        
                        # Sort links to prioritize documentation pages
                        new_links.sort(key=lambda link: 
                            0 if "/api/" in link or "/docs/" in link or "/reference/" in link or "/guides/" in link 
                            else 1
                        )
                        
                        for link in new_links:
                            if link not in visited_urls and link not in [url for url, _ in urls_to_visit]:
                                if len(visited_urls) + len(urls_to_visit) < limit:
                                    urls_to_visit.append((link, depth + 1))
                except Exception as e:
                    print(f"Error crawling {current_url}: {str(e)}")
                    continue
        finally:
            await browser.close()
    
    return results

def chunk_text(text, max_chars=1500):
    """Split text into chunks of max_chars."""
    # If text is shorter than max_chars, return it as a single chunk
    if len(text) <= max_chars:
        return [text]
    
    # Split text into paragraphs
    paragraphs = text.split('\n\n')
    
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        # If adding this paragraph would exceed max_chars, 
        # save current chunk and start a new one
        if len(current_chunk) + len(paragraph) + 2 > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph
        else:
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph
    
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def init_pinecone():
    """Initialize connection to Pinecone."""
    try:
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        if not pinecone_api_key:
            print("PINECONE_API_KEY not found in environment variables.")
            return None
            
        # Direct connection to the index host from the dashboard
        host = "https://mcp-index-3jg9lch.svc.aped-4627-b74a.pinecone.io"
        
        # Test connection by getting index stats
        headers = {
            "Api-Key": pinecone_api_key,
            "Accept": "application/json"
        }
        
        # Try to get index stats
        stats_url = f"{host}/describe_index_stats"
        response = requests.post(stats_url, headers=headers, json={})
        
        if response.status_code == 200:
            print("Successfully connected to Pinecone index!")
            print(f"Index stats: {response.json()}")
            
            # Return a dictionary with the host and headers for later use
            return {
                "host": host,
                "headers": headers
            }
        else:
            print(f"Connection to Pinecone failed with status code {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error initializing Pinecone: {e}")
        return None

def upload_to_pinecone(source_name, documents):
    """Upload documents to Pinecone vector database."""
    pinecone_conn = init_pinecone()
    if not pinecone_conn:
        print("Failed to initialize Pinecone connection.")
        return
    
    host = pinecone_conn["host"]
    headers = pinecone_conn["headers"]
    upsert_url = f"{host}/vectors/upsert"
    
    print(f"Uploading documents to Pinecone (source: {source_name})")
    
    # Create namespace from source name (replace invalid characters)
    namespace = re.sub(r'[^a-zA-Z0-9_-]', '_', source_name.lower())
    
    # Process documents in batches
    batch_size = 100
    count = 0
    total_vectors = 0
    
    for doc in documents:
        # Skip documents without markdown content
        if 'markdown' not in doc or not doc['markdown']:
            print(f"Skipping document without markdown content: {doc.get('url', 'unknown')}")
            continue
            
        # Get chunks of text
        chunks = chunk_text(doc['markdown'])
        
        # Extract metadata from document
        title = doc.get('title', '')
        url = doc.get('url', '')
            
        # For multilingual-e5-large model, we need 1024 dimensions
        dim = 1024
        
        # Process chunks in batches
        vectors_batch = []
        
        for i, chunk in enumerate(chunks):
            doc_id = f"{url.replace('://', '_').replace('/', '_')}_{i}"
            
            # Create a mock embedding vector
            # Note: In a production environment, you would use an actual embedding model
            mock_embedding = [0.01] * dim
            
            vectors_batch.append({
                "id": doc_id,
                "values": mock_embedding,
                "metadata": {
                    "title": title,
                    "url": url,
                    "chunk_index": i,
                    "text": chunk,  # Use 'text' field as specified in Pinecone dashboard
                    "source": source_name
                }
            })
            
            # Upload in batches
            if len(vectors_batch) >= batch_size:
                try:
                    upsert_data = {
                        "vectors": vectors_batch,
                        "namespace": namespace
                    }
                    
                    response = requests.post(upsert_url, headers=headers, json=upsert_data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        print(f"Uploaded {result.get('upsertedCount', len(vectors_batch))} vectors to Pinecone.")
                        total_vectors += result.get('upsertedCount', len(vectors_batch))
                    else:
                        print(f"Error uploading vectors to Pinecone: {response.status_code} - {response.text}")
                        
                    vectors_batch = []
                except Exception as e:
                    print(f"Error uploading vectors to Pinecone: {e}")
        
        count += 1
        
    # Upload any remaining vectors
    if vectors_batch:
        try:
            upsert_data = {
                "vectors": vectors_batch,
                "namespace": namespace
            }
            
            response = requests.post(upsert_url, headers=headers, json=upsert_data)
            
            if response.status_code == 200:
                result = response.json()
                print(f"Uploaded final {result.get('upsertedCount', len(vectors_batch))} vectors to Pinecone.")
                total_vectors += result.get('upsertedCount', len(vectors_batch))
            else:
                print(f"Error uploading final vectors to Pinecone: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Error uploading remaining vectors to Pinecone: {e}")
            
    print(f"Completed uploading {total_vectors} vectors to Pinecone namespace: {namespace}")

def save_crawl_results(results, base_url):
    """Save crawl results to files and database."""
    if not results:
        print("No data to save!")
        return
    
    # Create domain name for folder
    domain_name = get_domain_name(base_url)
    
    # Create directory for saving files
    output_dir = Path("docs") / domain_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save each result as a separate file
    for result in results:
        url = result.get("url", "")
        if not url:
            continue
        
        # Create filename from URL
        filename = create_filename(url, domain_name)
        
        # Save as JSON
        json_path = output_dir / f"{filename}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        # Save as Markdown
        markdown_path = output_dir / f"{filename}.md"
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(result.get("markdown", ""))
        
        print(f"Saved files: {json_path.name}, {markdown_path.name}")
    
    # Save full crawl result
    full_result_path = output_dir / "crawl_result.json"
    with open(full_result_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"All files saved to '{output_dir}' directory.")
    print(f"Full crawl result saved to '{full_result_path}'")
    
    # Save to PostgreSQL database
    try:
        # Create tables if they don't exist
        create_tables()
        print("Database tables created successfully.")
        
        # Save to database
        saved_count = save_to_postgres(results, base_url)
        print(f"Saved {saved_count} documents to PostgreSQL database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
    
    # Upload to Pinecone
    upload_to_pinecone(domain_name, results)

async def main_async():
    """Async main function."""
    parser = argparse.ArgumentParser(description="Crawl websites locally using Playwright.")
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument("--limit", type=int, default=5000, help="Maximum number of pages to crawl (default: 5000)")
    parser.add_argument("--max-depth", type=int, default=10, help="Maximum depth to crawl (default: 10)")
    parser.add_argument("--url-list", type=str, help="Path to a file containing URLs to crawl (one per line)")
    parser.add_argument("--timeout", type=int, default=120000, help="Page load timeout in milliseconds (default: 120000)")
    parser.add_argument("--sitemap-only", action="store_true", help="Only crawl URLs found in sitemap")
    
    args = parser.parse_args()
    
    print(f"Starting local crawl for: {args.url}")
    print(f"Limit: {args.limit}, Max Depth: {args.max_depth}")
    print(f"Timeout: {args.timeout}ms")
    
    start_time = time.time()
    
    # If URL list is provided, use those URLs
    if args.url_list:
        try:
            with open(args.url_list, 'r') as f:
                url_list = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(url_list)} URLs from {args.url_list}")
            
            # Override the crawl process to use the provided URLs
            results = []
            for i, url in enumerate(url_list[:args.limit]):
                try:
                    async with async_playwright() as p:
                        browser = await p.chromium.launch(headless=True)
                        context = await browser.new_context(
                            viewport={"width": 1280, "height": 800},
                            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                        )
                        page = await context.new_page()
                        
                        # Set the timeout
                        page.set_default_timeout(args.timeout)
                        
                        # Try to crawl with retry
                        max_retries = 2
                        for retry in range(max_retries + 1):
                            try:
                                result = await crawl_page(page, url)
                                results.append(result)
                                print(f"Crawled {i+1}/{len(url_list[:args.limit])} pages.")
                                break
                            except Exception as e:
                                if retry < max_retries:
                                    print(f"Attempt {retry+1} failed for {url}: {str(e)}. Retrying...")
                                    await asyncio.sleep(5)
                                else:
                                    print(f"All attempts failed for {url}: {str(e)}")
                                    results.append({
                                        "markdown": "",
                                        "metadata": {
                                            "title": "",
                                            "description": "",
                                            "sourceURL": url,
                                            "error": str(e)
                                        },
                                        "links": []
                                    })
                        
                        await browser.close()
                except Exception as e:
                    print(f"Error processing {url}: {str(e)}")
                    results.append({
                        "markdown": "",
                        "metadata": {
                            "title": "",
                            "description": "",
                            "sourceURL": url,
                            "error": str(e)
                        },
                        "links": []
                    })
            
            # Save results
            save_crawl_results(results, args.url)
            
            end_time = time.time()
            print(f"Crawl completed in {end_time - start_time:.2f} seconds.")
            print(f"Total pages crawled: {len(results)}")
            return
        except Exception as e:
            print(f"Error processing URL list: {str(e)}")
            return
    
    # If sitemap-only flag is set, only crawl URLs from sitemap
    if args.sitemap_only:
        print("Sitemap-only mode: Will only crawl URLs found in sitemap")
        try:
            sitemap_urls = await get_urls_from_sitemap(args.url)
            if not sitemap_urls:
                print("No URLs found in sitemap. Exiting.")
                return
            
            print(f"Found {len(sitemap_urls)} URLs in sitemap")
            
            # Write URLs to a temporary file
            temp_file = "temp_sitemap_urls.txt"
            with open(temp_file, 'w') as f:
                for url in sitemap_urls:
                    f.write(url + '\n')
            
            # Recursively call with url-list parameter
            print(f"Crawling URLs from sitemap...")
            await main_async_with_args(args.url, args.limit, args.max_depth, temp_file, args.timeout)
            
            # Clean up temporary file
            try:
                os.remove(temp_file)
            except Exception as e:
                print(f"Error removing temporary file: {str(e)}")
            
            return
        except Exception as e:
            print(f"Error processing sitemap: {str(e)}")
            # Continue with normal crawling
    
    try:
        # Crawl website
        results = await crawl_website(args.url, args.limit, args.max_depth)
        
        # Save results
        save_crawl_results(results, args.url)
        
        end_time = time.time()
        print(f"Crawl completed in {end_time - start_time:.2f} seconds.")
        print(f"Total pages crawled: {len(results)}")
    except Exception as e:
        print(f"Error during crawl: {str(e)}")

async def main_async_with_args(url, limit, max_depth, url_list=None, timeout=120000):
    """Run the crawler with the given arguments."""
    print(f"Starting local crawl of {url} with limit {limit} and max_depth {max_depth}")
    
    # Start timing
    start_time = time.time()
    
    # Create database tables if they don't exist
    try:
        create_tables()
        print("Database tables created/verified.")
    except Exception as e:
        print(f"Error creating database tables: {e}")
    
    # Crawl the website
    results = await crawl_website(url, limit, max_depth)
    
    # Save results
    save_crawl_results(results, url)
    
    print(f"Crawl completed in {time.time() - start_time:.2f} seconds.")
    print(f"Total pages crawled: {len(results)}")
    
    return results

def main():
    """Main function."""
    asyncio.run(main_async())

if __name__ == "__main__":
    main() 