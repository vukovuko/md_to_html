import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_basic_splitting(self):
        text = "# This is a heading\n\nThis is a paragraph.\n\n* Item 1\n* Item 2"
        result = markdown_to_blocks(text)
        expected = ["# This is a heading", "This is a paragraph.", "* Item 1\n* Item 2"]
        self.assertEqual(result, expected)

    def test_extra_newlines(self):
        text = "\n\n# Heading\n\n\nParagraph with **bold** text.\n\n\n* List item 1\n* List item 2\n\n"
        result = markdown_to_blocks(text)
        expected = [
            "# Heading",
            "Paragraph with **bold** text.",
            "* List item 1\n* List item 2",
        ]
        self.assertEqual(result, expected)

    def test_single_block(self):
        text = "# A single block"
        result = markdown_to_blocks(text)
        expected = ["# A single block"]
        self.assertEqual(result, expected)

    def test_only_newlines(self):
        text = "\n\n\n\n"
        result = markdown_to_blocks(text)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
