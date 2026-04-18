from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UN_LIST = "unordered list"
    O_LIST = "ordered list"

def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) >= 3 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith((">", "> ")):
        for line in lines:
            if not line.startswith((">", "> ")):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UN_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if line.startswith(f"{i}. "):
                i += 1
            else:
                return BlockType.PARAGRAPH
        return BlockType.O_LIST
            
    return BlockType.PARAGRAPH






def markdown_to_blocks(markdown):
    result = []
    temp = markdown.split("\n\n")
    for t in temp:
        i = t.strip()
        if i != "":
            result.append(i)
    return result