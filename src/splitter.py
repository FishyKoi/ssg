from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes; all others pass through unchanged
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # Split text by the delimiter
        parts = node.text.split(delimiter)

        # Odd number of parts = valid pairs; even = unmatched delimiter
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: missing closing delimiter '{delimiter}'")

        # Rebuild into new TextNodes
        for index, part in enumerate(parts):
            if index % 2 == 0:
                # Even index = normal text
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index = inside delimiter
                if not part:
                    raise ValueError("Empty delimited section is invalid")
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

from extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(node)
            continue

        parts = []
        remaining = text

        for alt, url in matches:
            pattern = f"![{alt}]({url})"
            before, remaining = remaining.split(pattern, 1)
            if before:
                parts.append(TextNode(before, TextType.TEXT))

            parts.append(TextNode(alt, TextType.IMAGE, url))

        if remaining:
            parts.append(TextNode(remaining, TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            continue

        parts = []
        remaining = text

        for anchor, url in matches:
            pattern = f"[{anchor}]({url})"
            before, remaining = remaining.split(pattern, 1)

            if before:
                parts.append(TextNode(before, TextType.TEXT))

            parts.append(TextNode(anchor, TextType.LINK, url))

        if remaining:
            parts.append(TextNode(remaining, TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes
