import unittest
from textnode import TextNode, TextType
from converter import text_node_to_html_node
from htmlnode import LeafNode

class TestTextNodeConversion(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_italic(self):
        node = TextNode("italics", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")

    def test_code(self):
        node = TextNode("print()", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "https://boot.dev")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://img.com/pic.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://img.com/pic.png")
        self.assertEqual(html_node.props["alt"], "alt text")

    def test_unknown_type(self):
        fake_node = TextNode("text", "unknown")
        with self.assertRaises(Exception):
            text_node_to_html_node(fake_node)

if __name__ == "__main__":
    unittest.main()
