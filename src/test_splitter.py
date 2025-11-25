import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_code_split(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_splits(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 5)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[3].text_type, TextType.CODE)

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[1].text, "bold")

    def test_italic_split(self):
        node = TextNode("Test _italic_ here", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[1].text, "italic")

    def test_no_closing_delimiter(self):
        node = TextNode("This is `broken text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_nodes_pass_through(self):
        node = TextNode("code", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result[0], node)

if __name__ == "__main__":
    unittest.main()
