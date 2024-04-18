# Triform.ai Template: HTML Content Cleaner

## Overview

This Python module serves as a template for cleaning HTML content, specifically focusing on extracting and sanitizing text from paragraphs while removing non-relevant sections and references. It is designed to integrate seamlessly into AI workflows on the Triform.ai platform.

## How it Works

The module parses HTML content provided in an event object, using BeautifulSoup for HTML parsing. It selectively extracts text from paragraph elements, excludes content within tables or 'infobox' classes, and cleans up references and HTML entities.

## Use Cases

- Preparing raw HTML content for text analysis or machine learning models.
- Cleaning web-scraped data to extract meaningful text content.

## Customization

To adapt this module for different types of content or HTML structures:
- Modify the `soup.find_all("p")` method to target different or additional tags.
- Adjust exclusion criteria based on the structure of your specific HTML data sources.
- Extend the regular expressions to handle other types of inline references or noise.
