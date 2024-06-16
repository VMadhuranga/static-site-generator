from parentnode import ParentNode
from leafnode import LeafNode


def convert_code_block(code_block):
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, code_block.strip("```\n").replace("\n", "&NewLine;"))])])
