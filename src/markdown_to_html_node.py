from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type


def text_to_children(text):
    """Converts inline markdown text into a list of HTMLNodes."""
    text_nodes = text_to_textnodes(text)
    return [
        LeafNode(
            None if node.text_type == "normal" else node.text_type,
            node.text,
            {"href": node.url} if node.text_type == "link" else None,
        )
        for node in text_nodes
    ]


def parse_heading(block):
    """Creates an HTMLNode for a heading block."""
    level = block.count("#", 0, block.find(" "))  # Count # at start
    text = block[level + 1 :]  # Remove heading markers
    return ParentNode(f"h{level}", text_to_children(text))


def parse_code(block):
    """Creates an HTMLNode for a code block."""
    text = block.strip("```")  # Remove triple backticks
    return ParentNode("pre", [ParentNode("code", text_to_children(text))])


def parse_quote(block):
    """Creates an HTMLNode for a quote block."""
    lines = [line.lstrip("> ") for line in block.split("\n")]
    text = " ".join(lines)
    return ParentNode("blockquote", text_to_children(text))


def parse_unordered_list(block):
    """Creates an HTMLNode for an unordered list block."""
    items = [line[2:] for line in block.split("\n")]
    children = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ul", children)


def parse_ordered_list(block):
    """Creates an HTMLNode for an ordered list block."""
    items = [line.split(". ", 1)[1] for line in block.split("\n")]
    children = [ParentNode("li", text_to_children(item)) for item in items]
    return ParentNode("ol", children)


def parse_paragraph(block):
    """Creates an HTMLNode for a paragraph block."""
    return ParentNode("p", text_to_children(block))


def markdown_to_html_node(markdown):
    """Converts full markdown document into an HTMLNode tree."""
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == "heading":
            block_nodes.append(parse_heading(block))
        elif block_type == "code":
            block_nodes.append(parse_code(block))
        elif block_type == "quote":
            block_nodes.append(parse_quote(block))
        elif block_type == "unordered_list":
            block_nodes.append(parse_unordered_list(block))
        elif block_type == "ordered_list":
            block_nodes.append(parse_ordered_list(block))
        else:
            block_nodes.append(parse_paragraph(block))

    return ParentNode("div", block_nodes)
