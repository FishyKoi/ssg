import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Test 1: Basic equality
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Test 2: Different text should NOT be equal
    def test_not_eq_text(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)
        self.assertNotEqual(node, node2)

    # Test 3: Different text_type should NOT be equal
    def test_not_eq_type(self):
        node = TextNode("Same text", TextType.TEXT)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Test 4: Different URL should NOT be equal
    def test_not_eq_url(self):
        node = TextNode("Link", TextType.LINK, "https://a.com")
        node2 = TextNode("Link", TextType.LINK, "https://b.com")
        self.assertNotEqual(node, node2)

    # Test 5: URL None equality
    def test_url_none(self):
        node = TextNode("Text", TextType.TEXT)
        node2 = TextNode("Text", TextType.TEXT, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
