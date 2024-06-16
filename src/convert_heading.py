from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def convert_heading(heading):
    heading_level, *contents = heading.split()
    tag = None

    if heading_level.count("#") == 1:
        tag = "h1"
    if heading_level.count("#") == 2:
        tag = "h2"
    if heading_level.count("#") == 3:
        tag = "h3"
    if heading_level.count("#") == 4:
        tag = "h4"
    if heading_level.count("#") == 5:
        tag = "h5"
    if heading_level.count("#") == 6:
        tag = "h6"

    text_nodes = text_to_textnodes(" ".join(contents))
    children = list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))
    heading_node = ParentNode(tag, children)
        
    return heading_node
