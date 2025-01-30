import re


def extract_markdown_images(text):
    """Extracts markdown image links from text and returns a list of (alt_text, url) tuples."""
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """Extracts markdown links from text and returns a list of (anchor_text, url) tuples."""
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
