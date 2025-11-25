import unittest
from extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_markdown_images_multiple(self):
        text = "![one](url1) and ![two](url2)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("one", "url1"), ("two", "url2")],
            matches
        )

    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "Here is a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [("link", "https://boot.dev")],
            matches
        )

    def test_extract_markdown_links_multiple(self):
        text = "Links: [a](url1) and [b](url2)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("a", "url1"), ("b", "url2")],
            matches
        )

    def test_extract_links_does_not_capture_images(self):
        text = "![img](url1) and [link](url2)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "url2")], matches)

if __name__ == "__main__":
    unittest.main()
