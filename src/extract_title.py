def extract_title(markdown):
    """
    Extract the first H1 (# ) title from markdown.
    Raise an exception if not found.
    """
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 title found in markdown")
