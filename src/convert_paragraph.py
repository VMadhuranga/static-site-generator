from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def convert_paragraph(paragraph):
    text_nodes = text_to_textnodes(paragraph.replace("\n", "<br />"))
    children = list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))
    return ParentNode("p", children)
