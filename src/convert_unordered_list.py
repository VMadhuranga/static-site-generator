import re

from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def convert_unordered_list(unordered_list):
    text_nodes = list(map(lambda item: text_to_textnodes(re.split(r"^[-/*] ", item)[1].strip()), unordered_list.split("\n")))
    children = list(map(lambda nodes: ParentNode("li", list(map(lambda node: text_node_to_html_node(node), nodes))), text_nodes))
    return ParentNode("ul", children)
