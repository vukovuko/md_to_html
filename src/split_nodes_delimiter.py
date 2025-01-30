from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Splits text nodes based on a delimiter, applying the given text type."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        for i, part in enumerate(parts):
            if part:
                new_nodes.append(
                    TextNode(part, text_type if i % 2 else TextType.NORMAL)
                )

    return new_nodes
