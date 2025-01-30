import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_image(self):
        node = TextNode(
            "This has an ![image](https://example.com/img.jpg) inside", TextType.NORMAL
        )
        result = split_nodes_image([node])
        expected = [
            TextNode("This has an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
            TextNode(" inside", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link(self):
        node = TextNode("Click [here](https://example.com) for more", TextType.NORMAL)
        result = split_nodes_link([node])
        expected = [
            TextNode("Click ", TextType.NORMAL),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" for more", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_mixed_text(self):
        node = TextNode(
            "Check this ![img](https://img.com) and [this](https://link.com)",
            TextType.NORMAL,
        )
        result = split_nodes_image([node])
        result = split_nodes_link(result)

        expected = [
            TextNode("Check this ", TextType.NORMAL),
            TextNode("img", TextType.IMAGE, "https://img.com"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("this", TextType.LINK, "https://link.com"),
        ]
        self.assertEqual(result, expected)

    def test_no_changes_needed(self):
        node = TextNode("Plain text with no links or images", TextType.NORMAL)
        result = split_nodes_image([node])
        result = split_nodes_link(result)
        self.assertEqual(result, [node])


if __name__ == "__main__":
    unittest.main()
