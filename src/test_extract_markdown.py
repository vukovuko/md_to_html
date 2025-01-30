import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):

    def test_extract_images(self):
        text = "This is ![image1](https://example.com/img1.png) and ![image2](https://example.com/img2.jpg)"
        expected = [
            ("image1", "https://example.com/img1.png"),
            ("image2", "https://example.com/img2.jpg"),
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_links(self):
        text = (
            "Here is [Google](https://google.com) and [Boot.dev](https://www.boot.dev)"
        )
        expected = [
            ("Google", "https://google.com"),
            ("Boot.dev", "https://www.boot.dev"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_mixed_text(self):
        text = (
            "An ![image](https://example.com/img.png) and a [link](https://example.com)"
        )
        self.assertEqual(
            extract_markdown_images(text), [("image", "https://example.com/img.png")]
        )
        self.assertEqual(
            extract_markdown_links(text), [("link", "https://example.com")]
        )

    def test_no_matches(self):
        text = "No markdown syntax here."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])


if __name__ == "__main__":
    unittest.main()
