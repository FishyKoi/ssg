import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    # Test 1: Paragraph tag
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    # Test 2: Anchor tag with props
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com">Click me!</a>'
        )

    # Test 3: No tag => raw text
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "just text")
        self.assertEqual(node.to_html(), "just text")

    # Test 4: Error on missing value
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    # Test 5: Props render correctly
    def test_leaf_props_multiple(self):
        node = LeafNode("span", "hi", {"class": "bold", "id": "x"})
        result = node.to_html()
        # order may vary in Python dicts, so check pieces
        self.assertTrue(result.startswith("<span "))
        self.assertIn('class="bold"', result)
        self.assertIn('id="x"', result)
        self.assertTrue(result.endswith(">hi</span>"))

if __name__ == "__main__":
    unittest.main()
