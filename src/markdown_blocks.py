def markdown_to_blocks(markdown):
    # Split into blocks where blank lines separate them
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        cleaned = block.strip()
        if cleaned:      # ignore empty blocks
            blocks.append(cleaned)

    return blocks
