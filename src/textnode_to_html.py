from leafnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    """Converts a TextNode to a corresponding LeafNode based on its TextType."""
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode instance.")

    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("TextNode of type LINK must have a URL.")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("TextNode of type IMAGE must have a URL.")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError("Invalid TextType in TextNode.")
