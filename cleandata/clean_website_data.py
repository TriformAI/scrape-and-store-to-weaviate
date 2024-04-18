import re
import json
import html
from bs4 import BeautifulSoup


def handler(event, context):
    # Extract the HTML content from the event object. This content is expected to be passed in 'output_0'.
    input_html = event.get("output_0")

    # Validate the input HTML content to ensure it's neither None nor empty.
    if not input_html:
        return json.dumps({"error": "No input HTML provided"})

    # Parse the input HTML content using BeautifulSoup with 'html.parser' as the parser.
    soup = BeautifulSoup(input_html, "html.parser")

    paragraphs = []
    # Iterate over all paragraph tags found in the HTML.
    for p in soup.find_all("p"):
        # Exclude paragraphs that are children of 'table' elements or have a parent with the 'infobox' class to avoid non-main content.
        if not p.find_parent("table") and not p.find_parent(class_="infobox"):
            # Convert HTML entities to their corresponding characters for each paragraph.
            paragraph_text = html.unescape(p.get_text())
            # Remove citations/references, identified by square brackets and numbers (e.g., "[1]"), from the paragraph text.
            cleaned_text = re.sub(r"\[\d+\]", "", paragraph_text)
            paragraphs.append(cleaned_text)

    # Join the cleaned paragraphs into a single string, separating them with spaces. Exclude any paragraphs that are empty or only contain whitespace.
    cleaned_html = " ".join([p for p in paragraphs if p.strip()])

    # Return the cleaned and combined HTML content as a JSON string with pretty-print formatting.
    return json.dumps({"output_0": cleaned_html}, indent=2)
