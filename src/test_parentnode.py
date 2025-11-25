import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    # Test 1: Basic parent with one child
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # Test 2: Parent with grandchildren (nested ParentNode)
    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # Test 3: Multiple mixed children
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " normal "),
                LeafNode("i", "italic"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b> normal <i>italic</i></p>"
        )

    # Test 4: Error when no tag
    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])

    # Test 5: Error when children is None
    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    # Test 6: Children must be a list
    def test_children_not_list(self):
        with self.assertRaises(ValueError):
            ParentNode("div", "not-a-list")

if __name__ == "__main__":
    unittest.main()
