from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from block_types import (
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_paragraph
)
from convert_heading import convert_heading
from convert_code_block import convert_code_block
from convert_quote_block import convert_quote_block
from convert_unordered_list import convert_unordered_list
from convert_ordered_list import convert_ordered_list
from convert_paragraph import convert_paragraph
from parentnode import ParentNode


def mark_down_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            children.append(convert_heading(block))
        elif block_to_block_type(block) == block_type_code:
            children.append(convert_code_block(block))
        elif block_to_block_type(block) == block_type_quote:
            children.append(convert_quote_block(block))
        elif block_to_block_type(block) == block_type_unordered_list:
            children.append(convert_unordered_list(block))
        elif block_to_block_type(block) == block_type_ordered_list:
            children.append(convert_ordered_list(block))
        elif block_to_block_type(block) == block_type_paragraph:
            children.append(convert_paragraph(block))

    return ParentNode("div" ,children)
