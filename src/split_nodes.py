from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    """Splits text nodes containing markdown images into separate TextNodes."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            sections = text.split(f"![{alt_text}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = sections[1] if len(sections) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes):
    """Splits text nodes containing markdown links into separate TextNodes."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for anchor_text, url in links:
            sections = text.split(f"[{anchor_text}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = sections[1] if len(sections) > 1 else ""

        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL))

    return new_nodes
