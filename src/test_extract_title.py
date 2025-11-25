import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_spaces(self):
        self.assertEqual(extract_title("   #   My Title   "), "My Title")

    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("No headings here\nJust text")

if __name__ == "__main__":
    unittest.main()
