import unittest
from textnode_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_text(self):
        node = text_node_to_html_node(TextNode("Plain text", TextType.NORMAL))
        self.assertEqual(node.to_html(), "Plain text")

    def test_text_type_bold(self):
        node = text_node_to_html_node(TextNode("Bold text", TextType.BOLD))
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        node = text_node_to_html_node(TextNode("Italic text", TextType.ITALIC))
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_text_type_code(self):
        node = text_node_to_html_node(TextNode("Code snippet", TextType.CODE))
        self.assertEqual(node.to_html(), "<code>Code snippet</code>")

    def test_text_type_link(self):
        node = text_node_to_html_node(
            TextNode("Click here", TextType.LINK, "https://example.com")
        )
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_text_type_image(self):
        node = text_node_to_html_node(
            TextNode("Image alt text", TextType.IMAGE, "https://example.com/image.jpg")
        )
        self.assertEqual(
            node.to_html(),
            '<img src="https://example.com/image.jpg" alt="Image alt text">',
        )

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid", None))

    def test_link_without_url_raises_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("No URL", TextType.LINK))

    def test_image_without_url_raises_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("No URL", TextType.IMAGE))


if __name__ == "__main__":
    unittest.main()
