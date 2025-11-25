import unittest
from textnode import TextNode, TextType
from splitter import split_nodes_image, split_nodes_link

class TestSplitNodesSpecial(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_none(self):
        node = TextNode("Nothing here", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result[0].text, "Nothing here")

    def test_split_links(self):
        node = TextNode(
            "Link to [boot](https://boot.dev) and [youtube](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("Link to ", TextType.TEXT),
                TextNode("boot", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes
        )

    def test_split_links_none(self):
        node = TextNode("No links here", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result[0].text, "No links here")

    def test_non_text_nodes_untouched(self):
        node = TextNode("ignore", TextType.BOLD)
        result1 = split_nodes_image([node])
        result2 = split_nodes_link([node])
        self.assertEqual(result1[0], node)
        self.assertEqual(result2[0], node)

if __name__ == "__main__":
    unittest.main()
