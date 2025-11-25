import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown
    with open(from_path, "r") as f:
        markdown = f.read()

    # Read template
    with open(template_path, "r") as f:
        template = f.read()

    # Convert Markdown -> HTML
    html_node = markdown_to_html_node(markdown)
    content_html = html_node.to_html()

    # Extract <title>
    title = extract_title(markdown)

    # Replace placeholders
    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", content_html)

    # Ensure destination folder exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write page
    with open(dest_path, "w") as f:
        f.write(full_html)
