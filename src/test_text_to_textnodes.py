import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_basic_text(self):
        text = "Just a normal sentence."
        result = text_to_textnodes(text)
        expected = [TextNode("Just a normal sentence.", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_text_with_bold(self):
        text = "This is **bold** text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_italic(self):
        text = "This is *italic* text."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_code(self):
        text = "Some `code block` here."
        result = text_to_textnodes(text)
        expected = [
            TextNode("Some ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" here.", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_image(self):
        text = "This is an ![image](https://example.com/img.jpg)."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_link(self):
        text = "Visit [Boot.dev](https://boot.dev) for coding!"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Visit ", TextType.NORMAL),
            TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            TextNode(" for coding!", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_complex_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
