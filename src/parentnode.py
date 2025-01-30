from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have at least one child.")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """Recursively renders the ParentNode and its children as an HTML string."""
        if self.children is None:
            raise ValueError("ParentNode must have children.")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
