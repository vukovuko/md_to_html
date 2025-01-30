import re


def block_to_block_type(block):
    """Determines the type of a markdown block."""

    if re.match(r"^#{1,6} ", block):
        return "heading"

    if block.startswith("```") and block.endswith("```"):
        return "code"

    if all(line.startswith(">") for line in block.split("\n")):
        return "quote"

    if all(re.match(r"^(\*|-) ", line) for line in block.split("\n")):
        return "unordered_list"

    lines = block.split("\n")
    if all(re.match(rf"^{i+1}\. ", lines[i]) for i in range(len(lines))):
        return "ordered_list"

    return "paragraph"
