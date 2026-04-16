from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        if node.text_type == TextType.TEXT:
            extracted_text = extract_markdown_images(node.text)
            remaining_text = node.text
            for alt, url in extracted_text:
                sections = remaining_text.split(f"![{alt}]({url})", 1)
                if sections[0] != "":
                    result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(alt, TextType.IMAGE, url))
                remaining_text = sections[1]
            if remaining_text != "":
                result.append(TextNode(remaining_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
        result = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                result.append(node)
                continue
            if node.text_type == TextType.TEXT:
                extracted_text = extract_markdown_links(node.text)
                remaining_text = node.text
                for alt, url in extracted_text:
                    sections = remaining_text.split(f"[{alt}]({url})", 1)
                    if sections[0] != "":
                        result.append(TextNode(sections[0], TextType.TEXT))
                    result.append(TextNode(alt, TextType.LINK, url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    result.append(TextNode(remaining_text, TextType.TEXT))
        return result