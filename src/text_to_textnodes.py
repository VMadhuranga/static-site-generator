from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from text_types import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def text_to_textnodes(text):
    nodes = split_nodes_image([TextNode(text, text_type_text)])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "__", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "_", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    return nodes
