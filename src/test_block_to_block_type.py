import unittest
from block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("## Subheading"), "heading")
        self.assertEqual(block_to_block_type("###### Smallest Heading"), "heading")

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello')\n```"), "code")
        self.assertEqual(block_to_block_type("```\ncode block\nline 2\n```"), "code")

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2\n> Line 3"), "quote")

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item A\n- Item B"), "unordered_list")

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. First\n2. Second\n3. Third"), "ordered_list"
        )

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph of text."), "paragraph"
        )
        self.assertEqual(
            block_to_block_type("Another line of normal text."), "paragraph"
        )


if __name__ == "__main__":
    unittest.main()
