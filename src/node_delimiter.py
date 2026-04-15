from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        if node.text_type == TextType.TEXT:
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Invalid markdown")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    result.append(TextNode(sections[i], TextType.TEXT))
                if i % 2 != 0:
                    result.append(TextNode(sections[i], text_type))
    return result
        