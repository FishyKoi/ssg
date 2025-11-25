from markdown_blocks import markdown_to_blocks
from block_classifier import block_to_block_type
from blocktype import BlockType
from htmlnode import ParentNode
from textprocessor import text_to_textnodes
from converter import text_node_to_html_node
from textnode import TextNode, TextType


def text_to_children(text):
    """Convert inline markdown text into HTMLNode children."""
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]


def handle_paragraph(block):
    # Paragraphs can span multiple lines → join them
    lines = block.split("\n")
    joined = " ".join(lines)
    children = text_to_children(joined)
    return ParentNode("p", children)


def handle_heading(block):
    # Count leading '#'
    count = 0
    while count < len(block) and block[count] == "#":
        count += 1

    # Remove "#... "
    text = block[count + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{count}", children)


def handle_code(block):
    # Strip the ``` fences
    lines = block.split("\n")
    content = "\n".join(lines[1:-1]) + "\n"

    textnode = TextNode(content, TextType.TEXT)
    child = text_node_to_html_node(textnode)

    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def handle_quote(block):
    # Remove leading "> "
    lines = block.split("\n")
    cleaned = [line[2:] for line in lines]
    text = " ".join(cleaned)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def handle_unordered_list(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        item_text = line[2:]
        item_children = text_to_children(item_text)
        items.append(ParentNode("li", item_children))
    return ParentNode("ul", items)


def handle_ordered_list(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        # remove "1. "
        index = line.find(". ")
        item_text = line[index + 2 :]
        item_children = text_to_children(item_text)
        items.append(ParentNode("li", item_children))
    return ParentNode("ol", items)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.PARAGRAPH:
            children.append(handle_paragraph(block))

        elif btype == BlockType.HEADING:
            children.append(handle_heading(block))

        elif btype == BlockType.CODE:
            children.append(handle_code(block))

        elif btype == BlockType.QUOTE:
            children.append(handle_quote(block))

        elif btype == BlockType.UNORDERED_LIST:
            children.append(handle_unordered_list(block))

        elif btype == BlockType.ORDERED_LIST:
            children.append(handle_ordered_list(block))

        else:
            # fallback paragraph
            children.append(handle_paragraph(block))

    return ParentNode("div", children)
