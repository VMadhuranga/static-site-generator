import re

from textnode import TextNode
from text_types import (
    text_type_text,
    text_type_image
)


def split_nodes_image(old_nodes):
    new_nodes =[]

    for node in old_nodes:
        node_text = node.text
        node_text_type = node.text_type

        if node_text_type != text_type_text:
            new_nodes.append(node)
            continue

        splitted_node_text = re.split(r"!\[(.*?)\]\((.*?)\)", node_text)
        for i in range(0, len(splitted_node_text), 3):
            if i != 0:
                alt_text = splitted_node_text[i - 2]
                url = splitted_node_text[i - 1]

                if alt_text != "" or url != "":
                    new_nodes.append(TextNode(alt_text, text_type_image, url))

            if splitted_node_text[i] != "":
                new_nodes.append(TextNode(splitted_node_text[i], node_text_type))

    return new_nodes
