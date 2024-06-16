import re

from textnode import TextNode
from text_types import (
    text_type_text,
    text_type_link
)


def split_nodes_link(old_nodes):
    new_nodes =[]

    for node in old_nodes:
        node_text = node.text
        node_text_type = node.text_type

        if node_text_type != text_type_text:
            new_nodes.append(node)
            continue

        splitted_node_text = re.split(r"\[(.*?)\]\((.*?)\)", node_text)
        for i in range(0, len(splitted_node_text), 3):
            if i != 0:
                link_text = splitted_node_text[i - 2]
                url = splitted_node_text[i - 1]

                if link_text != "" or url != "":
                    new_nodes.append(TextNode(link_text, text_type_link, url))

            if splitted_node_text[i] != "":
                new_nodes.append(TextNode(splitted_node_text[i], node_text_type))

    return new_nodes
