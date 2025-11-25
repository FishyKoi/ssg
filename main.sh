#!/bin/bash
set -e

echo "Generating site..."

PYTHONPATH=src python3 - <<EOF
from copy_static import copy_static
# If you have your generator file, import it here
# from generate_html import generate_site

copy_static("static", "public")

# If generator exists, enable this:
# generate_site("content", "template.html", "public")
EOF

echo "Done!"
