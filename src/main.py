import sys
import os
from markdown_to_html_node import markdown_to_html_node
from copy_static import copy_static


def generate_page(markdown_path, template_path, dest_path, basepath):
    with open(markdown_path, "r") as f:
        markdown = f.read()

    # Convert markdown using the DOM-based converter
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    with open(template_path, "r") as f:
        template = f.read()

    page_html = template.replace("{{ Title }}", get_title_from_markdown(markdown))
    page_html = page_html.replace("{{ Content }}", html_content)

    # Fix basepath for GitHub Pages
    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page_html)


def get_title_from_markdown(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:]
    return "Untitled"


def generate_pages_recursive(content_dir, template_path, dest_dir, basepath):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)

                rel_path = os.path.relpath(md_path, content_dir)
                rel_no_ext = os.path.splitext(rel_path)[0]
                dest_file = os.path.join(dest_dir, rel_no_ext + ".html")

                generate_page(md_path, template_path, dest_file, basepath)


def main():
    # Basepath handling
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"

    # GitHub Pages uses docs/, not public/
    dest_dir = "docs"

    if os.path.exists(dest_dir):
        # Clean old build
        for root, dirs, files in os.walk(dest_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for d in dirs:
                os.rmdir(os.path.join(root, d))

    os.makedirs(dest_dir, exist_ok=True)

    copy_static("static", dest_dir)
    generate_pages_recursive("content", "template.html", dest_dir, basepath)


if __name__ == "__main__":
    main()
