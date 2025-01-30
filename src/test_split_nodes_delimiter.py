import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_with_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_split_with_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_split_with_italic_delimiter(self):
        node = TextNode("An *italic* word", TextType.NORMAL)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("An ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_raises_error_on_unmatched_delimiters(self):
        node = TextNode("This is **bold but missing", TextType.NORMAL)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_splits_in_one_text(self):
        node = TextNode("Mixing *italic* and **bold** here", TextType.NORMAL)

        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "*", TextType.ITALIC)

        expected = [
            TextNode("Mixing ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" here", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
