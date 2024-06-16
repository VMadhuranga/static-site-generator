import re

from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def convert_quote_block(quote_block):
    text_nodes = text_to_textnodes(" ".join(list(map(lambda item: item.strip("> "), quote_block.split("\n")))))
    children = list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))
    return ParentNode("blockquote", children)
