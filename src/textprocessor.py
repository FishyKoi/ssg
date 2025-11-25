from textnode import TextNode, TextType
from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # Order matters:
    # 1. Code
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # 2. Bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # 3. Italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # 4. Images
    nodes = split_nodes_image(nodes)

    # 5. Links
    nodes = split_nodes_link(nodes)

    return nodes
