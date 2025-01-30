import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parentnode_without_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Text")])

    def test_parentnode_without_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_parentnode_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "More normal text"),
            ],
        )
        expected_html = (
            "<p><b>Bold text</b>Normal text<i>Italic text</i>More normal text</p>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_parentnode(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold"),
                        LeafNode(None, " Normal text"),
                    ],
                ),
                LeafNode("i", "Italic"),
            ],
        )
        expected_html = "<div><p><b>Bold</b> Normal text</p><i>Italic</i></div>"
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
