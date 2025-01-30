import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_values(self):
        """Test equality when all properties are the same"""
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_with_url(self):
        """Test equality when all properties including URL are the same"""
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        """Test inequality when text is different"""
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Goodbye", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        """Test inequality when text_type is different"""
        node1 = TextNode("Some text", TextType.BOLD)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
        """Test inequality when URL is different"""
        node1 = TextNode("A link", TextType.LINK, "https://example.com")
        node2 = TextNode("A link", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_none(self):
        """Test that the default URL is None"""
        node = TextNode("Plain text", TextType.NORMAL)
        self.assertIsNone(node.url)

    def test_repr_output(self):
        """Test the string representation (__repr__) of TextNode"""
        node = TextNode("Test", TextType.BOLD, "https://test.com")
        self.assertEqual(repr(node), "TextNode(Test, bold, https://test.com)")


if __name__ == "__main__":
    unittest.main()
