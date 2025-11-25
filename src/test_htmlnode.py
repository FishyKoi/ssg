import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    # Test 1: props_to_html with multiple props
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    # Test 2: empty props returns empty string
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    # Test 3: None props returns empty string
    def test_props_to_html_none(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
