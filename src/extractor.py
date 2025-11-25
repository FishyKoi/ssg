import re

def extract_markdown_images(text):
    # Pattern: ![alt text](url)
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Pattern: [anchor text](url)
    # Must NOT match images (Images start with '!')
    pattern = r"(?<!!)\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, text)
    return matches
