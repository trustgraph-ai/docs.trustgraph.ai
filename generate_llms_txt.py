#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt from Jekyll-generated _site directory.

This script parses the HTML files in the _site directory and extracts content
to create LLM-friendly text files for documentation context.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urljoin, urlparse
import argparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: BeautifulSoup4 is required. Install with: pip install beautifulsoup4")
    sys.exit(1)

class DocumentationParser:
    def __init__(self, site_dir: str, base_url: str = "https://docs.trustgraph.ai"):
        self.site_dir = Path(site_dir)
        self.base_url = base_url
        self.pages = []
        self.navigation_order = [
            "getting-started",
            "overview", 
            "deployment",
            "guides",
            "reference",
            "examples",
            "advanced",
            "community"
        ]
        
    def clean_text(self, text: str) -> str:
        """Clean and normalize text content."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        # Remove Jekyll/HTML artifacts
        text = re.sub(r'{%.*? %}', '', text)
        text = re.sub(r'{{.*?}}', '', text)
        # Clean up common HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&amp;', '&')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        return text
        
    def extract_navigation_info(self, soup: BeautifulSoup) -> Dict[str, str]:
        """Extract navigation metadata from the page."""
        nav_info = {}
        
        # Look for navigation elements
        nav_parent = soup.find('nav', class_='navigation')
        if nav_parent:
            # Extract breadcrumb or parent information
            breadcrumb = nav_parent.find('ol', class_='breadcrumb-nav')
            if breadcrumb:
                nav_info['breadcrumb'] = [item.get_text().strip() for item in breadcrumb.find_all('li')]
        
        # Extract title
        title_elem = soup.find('h1') or soup.find('title')
        if title_elem:
            nav_info['title'] = self.clean_text(title_elem.get_text())
            
        return nav_info
        
    def extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from the page."""
        # Remove navigation, footer, and other non-content elements
        for element in soup.find_all(['nav', 'footer', 'header', 'aside']):
            element.decompose()
            
        # Remove script and style elements
        for element in soup.find_all(['script', 'style']):
            element.decompose()
            
        # Try to find main content area
        main_content = soup.find('main') or soup.find('div', class_='main-content') or soup.find('div', id='main-content')
        
        if main_content:
            content = main_content.get_text(separator='\n')
        else:
            # Fallback to body content
            body = soup.find('body')
            if body:
                content = body.get_text(separator='\n')
            else:
                content = soup.get_text(separator='\n')
                
        return self.clean_text(content)
        
    def get_page_priority(self, file_path: str) -> int:
        """Determine page priority based on path for ordering."""
        path_parts = file_path.split('/')
        
        # Index pages get higher priority
        if 'index.html' in file_path:
            return 0
            
        # Order by navigation structure
        for i, section in enumerate(self.navigation_order):
            if section in path_parts:
                return i + 1
                
        # Default priority
        return 999
        
    def parse_site(self) -> List[Dict]:
        """Parse all HTML files in the site directory."""
        html_files = list(self.site_dir.glob('**/*.html'))
        
        for html_file in html_files:
            # Skip certain files
            if any(skip in str(html_file) for skip in ['404.html', 'search.html', 'assets/']):
                continue
                
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    
                # Extract relative path from site directory
                rel_path = str(html_file.relative_to(self.site_dir))
                
                # Extract content and metadata
                nav_info = self.extract_navigation_info(soup)
                content = self.extract_content(soup)
                
                # Skip if no meaningful content
                if len(content.strip()) < 50:
                    continue
                    
                page_info = {
                    'path': rel_path,
                    'url': urljoin(self.base_url, rel_path),
                    'title': nav_info.get('title', 'Untitled'),
                    'content': content,
                    'priority': self.get_page_priority(rel_path),
                    'breadcrumb': nav_info.get('breadcrumb', [])
                }
                
                self.pages.append(page_info)
                
            except Exception as e:
                print(f"Error parsing {html_file}: {e}")
                continue
                
        # Sort pages by priority and then by path
        self.pages.sort(key=lambda x: (x['priority'], x['path']))
        return self.pages
        
    def generate_llms_txt(self) -> str:
        """Generate condensed llms.txt content."""
        content = ["# TrustGraph Documentation"]
        content.append("")
        content.append("TrustGraph is a powerful graph database and analytics platform designed for trust and reputation systems.")
        content.append("")
        
        # Group pages by section
        sections = {}
        for page in self.pages:
            section = page['path'].split('/')[0]
            if section not in sections:
                sections[section] = []
            sections[section].append(page)
            
        # Add navigation overview
        content.append("## Documentation Structure")
        content.append("")
        
        for section_name in self.navigation_order:
            if section_name in sections:
                section_pages = sections[section_name]
                index_page = next((p for p in section_pages if 'index.html' in p['path']), None)
                
                if index_page:
                    content.append(f"### {index_page['title']}")
                    # Add first few lines of content as summary
                    summary_lines = index_page['content'].split('\n')[:3]
                    content.extend(summary_lines)
                    content.append("")
                    
                    # List sub-pages
                    sub_pages = [p for p in section_pages if p != index_page]
                    if sub_pages:
                        content.append("Sub-sections:")
                        for sub_page in sub_pages[:5]:  # Limit to first 5
                            content.append(f"- {sub_page['title']}")
                        content.append("")
                        
        # Add key concepts from getting started
        getting_started = next((p for p in self.pages if 'getting-started/index.html' in p['path']), None)
        if getting_started:
            content.append("## Key Concepts")
            content.append("")
            lines = getting_started['content'].split('\n')
            for line in lines:
                if any(keyword in line.lower() for keyword in ['concept', 'fundamental', 'core', 'basic']):
                    content.append(line)
                    
        return '\n'.join(content)
        
    def generate_llms_full_txt(self) -> str:
        """Generate complete llms-full.txt content."""
        content = ["# TrustGraph Documentation - Complete Reference"]
        content.append("")
        content.append("This document contains the complete TrustGraph documentation for LLM context.")
        content.append("")
        
        current_section = None
        for page in self.pages:
            section = page['path'].split('/')[0]
            
            # Add section header if we're in a new section
            if section != current_section:
                current_section = section
                content.append(f"\n# {section.replace('-', ' ').title()}")
                content.append("=" * 50)
                content.append("")
                
            # Add page content
            content.append(f"## {page['title']}")
            content.append(f"URL: {page['url']}")
            content.append("")
            content.append(page['content'])
            content.append("")
            content.append("-" * 40)
            content.append("")
            
        return '\n'.join(content)

def main():
    parser = argparse.ArgumentParser(description='Generate llms.txt and llms-full.txt from Jekyll site')
    parser.add_argument('--site-dir', default='_site', help='Path to Jekyll _site directory')
    parser.add_argument('--base-url', default='https://docs.trustgraph.ai', help='Base URL for the documentation')
    parser.add_argument('--output-dir', default='.', help='Output directory for generated files')
    
    args = parser.parse_args()
    
    # Check if site directory exists
    if not os.path.exists(args.site_dir):
        print(f"Error: Site directory '{args.site_dir}' does not exist.")
        print("Make sure to run 'bundle exec jekyll build' first.")
        sys.exit(1)
        
    # Initialize parser
    doc_parser = DocumentationParser(args.site_dir, args.base_url)
    
    print("Parsing documentation site...")
    pages = doc_parser.parse_site()
    print(f"Found {len(pages)} pages")
    
    # Generate llms.txt
    print("Generating llms.txt...")
    llms_content = doc_parser.generate_llms_txt()
    llms_path = os.path.join(args.output_dir, 'llms.txt')
    with open(llms_path, 'w', encoding='utf-8') as f:
        f.write(llms_content)
    print(f"Generated {llms_path} ({len(llms_content)} characters)")
    
    # Generate llms-full.txt
    print("Generating llms-full.txt...")
    llms_full_content = doc_parser.generate_llms_full_txt()
    llms_full_path = os.path.join(args.output_dir, 'llms-full.txt')
    with open(llms_full_path, 'w', encoding='utf-8') as f:
        f.write(llms_full_content)
    print(f"Generated {llms_full_path} ({len(llms_full_content)} characters)")
    
    print("Done!")

if __name__ == '__main__':
    main()