from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    VOID_ELEMENTS = {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "source",
        "track",
        "wbr",
    }

    def __init__(self, tag, value, props=None):
        if value is None and tag not in self.VOID_ELEMENTS:
            raise ValueError("LeafNode must have a value unless it's a void element.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """Renders the LeafNode as an HTML string."""
        if self.tag is None:
            return self.value

        if self.tag in self.VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()}>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
