import shutil
from copy_static import copy_static
from generate_page import generate_page


def main():
    # Clear public directory
    shutil.rmtree("public", ignore_errors=True)

    # Copy static files
    copy_static("static", "public")

    # Generate index.html
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
