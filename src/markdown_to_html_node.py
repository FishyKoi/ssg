from htmlnode import ParentNode, LeafNode
from textprocessor import text_to_textnodes
from markdown_blocks import markdown_to_blocks
from block_classifier import block_to_block_type
from blocktype import BlockType
from converter import text_node_to_html_node


def convert_inline_text(text):
    """
    Convert a raw inline markdown string
    into a list of HTML nodes (<b>, <i>, <code>, <a>, <img>, text).
    """
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        # -------------------------
        # PARAGRAPH
        # -------------------------
        if block_type == BlockType.PARAGRAPH:
            inline = convert_inline_text(block)
            children.append(ParentNode("p", inline))

        # -------------------------
        # HEADING (#, ##, ###...)
        # -------------------------
        elif block_type == BlockType.HEADING:
            level = block.count("#", 0, block.find(" "))
            content = block[level + 1:].strip()
            inline = convert_inline_text(content)
            children.append(ParentNode(f"h{level}", inline))

        # -------------------------
        # CODE BLOCK
        # -------------------------
        elif block_type == BlockType.CODE:
            body = block.strip("`").strip()
            code_node = LeafNode(None, body)
            children.append(ParentNode("pre", [ParentNode("code", [code_node])]))

        # -------------------------
        # BLOCKQUOTE
        # -------------------------
        elif block_type == BlockType.QUOTE:
            inner = "\n".join(line.lstrip("> ").rstrip() for line in block.split("\n"))
            inline = convert_inline_text(inner)
            children.append(ParentNode("blockquote", inline))

        # -------------------------
        # BULLETED LIST
        # -------------------------
        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                content = line.lstrip("*- ").rstrip()
                inline = convert_inline_text(content)
                items.append(ParentNode("li", inline))
            children.append(ParentNode("ul", items))

        # -------------------------
        # ORDERED LIST
        # -------------------------
        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                content = line.split(".", 1)[1].strip()
                inline = convert_inline_text(content)
                items.append(ParentNode("li", inline))
            children.append(ParentNode("ol", items))

        # -------------------------
        # FALLBACK → treat as paragraph
        # -------------------------
        else:
            inline = convert_inline_text(block)
            children.append(ParentNode("p", inline))

    return ParentNode("div", children)
