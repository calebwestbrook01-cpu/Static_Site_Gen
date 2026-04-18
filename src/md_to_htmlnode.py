from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    result = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            h = len(block) - len(block.lstrip("#"))
            stripped = block[h + 1:]
            tag_head = f"h{h}"
            block_nodes.append(ParentNode(tag_head, text_to_children(stripped)))
        if block_type == BlockType.CODE:
            code_text = TextNode(block[4:-3], TextType.TEXT)
            code_html = text_node_to_html_node(code_text)
            code_node = ParentNode("code", [code_html])
            block_nodes.append(ParentNode("pre", [code_node]))
        if block_type == BlockType.QUOTE:
            quotes = block.split("\n")
            new_quotes = []
            for quote in quotes:
                new_quote = quote.lstrip("> ")
                new_quotes.append(new_quote)
            final_quotes = " ".join(new_quotes)
            block_nodes.append(ParentNode("blockquote", text_to_children(final_quotes)))
        if block_type == BlockType.UN_LIST:
            unlist_lines = block.split("\n")
            li_nodes = []
            for line in unlist_lines:
                new_un = line[2:]
                li_nodes.append(ParentNode("li", text_to_children(new_un)))
            block_nodes.append(ParentNode("ul", li_nodes))
        if block_type == BlockType.O_LIST:
            olist_lines = block.split("\n")
            oli_nodes = []
            for line in olist_lines:
                new_o = line[3:]
                oli_nodes.append(ParentNode("li", text_to_children(new_o)))
            block_nodes.append(ParentNode("ol", oli_nodes))
        if block_type == BlockType.PARAGRAPH:
            para_lines = block.split("\n")
            final_para = " ".join(para_lines)
            block_nodes.append(ParentNode("p", text_to_children(final_para)))
    return ParentNode("div", block_nodes)
        


            

