def markdown_to_blocks(markdown):
    """Splits a markdown document into block-level elements separated by blank lines."""
    blocks = [block.strip() for block in markdown.strip().split("\n\n")]
    return [block for block in blocks if block]  # Remove empty blocks
