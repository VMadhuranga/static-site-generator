import re

from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def convert_ordered_list(ordered_list):
    text_nodes = list(map(lambda item: text_to_textnodes(re.split(r"^\d+. ", item)[1].strip()), ordered_list.split("\n")))
    children = list(map(lambda nodes: ParentNode("li", list(map(lambda node: text_node_to_html_node(node), nodes))), text_nodes))
    return ParentNode("ol", children)
