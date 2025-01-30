import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_heading(self):
        md = "# Heading"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")

    def test_code_block(self):
        md = "```\nprint('Hello')\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><pre><code>print('Hello')</code></pre></div>"
        )

    def test_quote(self):
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><blockquote>This is a quote</blockquote></div>"
        )

    def test_unordered_list(self):
        md = "* Item 1\n* Item 2"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )

    def test_ordered_list(self):
        md = "1. First\n2. Second"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><ol><li>First</li><li>Second</li></ol></div>"
        )

    def test_paragraph(self):
        md = "This is a paragraph."
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph.</p></div>")

    def test_full_document(self):
        md = "# Title\n\nThis is a paragraph.\n\n* Bullet 1\n* Bullet 2"
        node = markdown_to_html_node(md)
        expected = "<div><h1>Title</h1><p>This is a paragraph.</p><ul><li>Bullet 1</li><li>Bullet 2</li></ul></div>"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
