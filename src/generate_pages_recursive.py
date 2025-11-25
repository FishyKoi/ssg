import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively walk the content/ directory.
    For every .md file, generate the matching .html file
    inside public/ with identical directory structure.
    """

    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # If directory → recurse
        if os.path.isdir(full_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(full_path, template_path, dest_path)

        # If markdown file → generate HTML
        elif entry.endswith(".md"):
            html_name = entry.replace(".md", ".html")
            dest_file = os.path.join(dest_dir_path, html_name)
            generate_page(full_path, template_path, dest_file)
