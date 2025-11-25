import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "Just one paragraph here."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one paragraph here."])

    def test_remove_multiple_empty_lines(self):
        md = "Line1\n\n\n\nLine2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line1", "Line2"])

if __name__ == "__main__":
    unittest.main()
