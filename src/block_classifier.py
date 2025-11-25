from blocktype import BlockType

def block_to_block_type(block):
    lines = block.split("\n")

    # ---- HEADING ----
    # 1-6 # characters + space
    if lines[0].startswith("#"):
        i = 0
        while i < len(lines[0]) and lines[0][i] == "#":
            i += 1
        if 1 <= i <= 6 and len(lines[0]) > i and lines[0][i] == " ":
            return BlockType.HEADING

    # ---- CODE BLOCK ----
    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE

    # ---- QUOTE BLOCK ----
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # ---- UNORDERED LIST ----
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # ---- ORDERED LIST ----
    # Every line: number. space
    is_ordered = True
    expected_number = 1

    for line in lines:
        if not line.startswith(f"{expected_number}. "):
            is_ordered = False
            break
        expected_number += 1

    if is_ordered and len(lines) > 1:
        return BlockType.ORDERED_LIST

    # ---- PARAGRAPH ----
    return BlockType.PARAGRAPH
