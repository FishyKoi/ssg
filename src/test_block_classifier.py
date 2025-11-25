import unittest
from block_classifier import block_to_block_type
from blocktype import BlockType

class TestBlockClassifier(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Mid"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Small"), BlockType.HEADING)

    def test_not_heading_missing_space(self):
        self.assertEqual(block_to_block_type("####NoSpace"), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\ncode inside\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> quote\n> more"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item1\n- item2\n- item3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. One\n2. Two\n3. Three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_numbers(self):
        block = "1. One\n3. Wrong"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        block = "Just a normal paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
