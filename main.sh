#!/bin/bash
set -e

# Run the generator
PYTHONPATH=src python3 src/main.py

# Start server
cd public
python3 -m http.server 8888
