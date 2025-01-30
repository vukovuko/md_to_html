import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode_without_tag(self):
        node = LeafNode(None, "Plain text")
        self.assertEqual(node.to_html(), "Plain text")

    def test_leafnode_with_tag(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leafnode_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leafnode_without_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)


if __name__ == "__main__":
    unittest.main()
