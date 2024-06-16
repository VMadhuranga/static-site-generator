from textnode import TextNode
from text_types import text_type_text


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        node_text_type = node.text_type
        if node_text_type != text_type_text:
            new_nodes.append(node)
            continue

        node_text = node.text
        if node_text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown syntax")
        
        splitted_node_text = node_text.split(delimiter)
        for i, text in enumerate(splitted_node_text):
            if text == "":
                continue

            if i % 2 != 0:
                new_nodes.append(TextNode(text, text_type)) 
            else:
                new_nodes.append(TextNode(text, node_text_type))

    return new_nodes
