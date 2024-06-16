import re

from functools import reduce
from block_types import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
) 


def block_to_block_type(block):
    heading_regex = r"^#{1,6} .*$"
    code_block_regex = r"^```\n.*\n```$"
    block_quote_regex = r"^> .*$"
    unordered_list_regex = r"^[-|*] .*$"
    ordered_list_regex = r"^\d\. .*$"

    if re.match(heading_regex, block):
        return block_type_heading
    if re.match(code_block_regex, block, flags=re.M|re.S):
        return block_type_code

    splitted_block = block.split("\n")
    if reduce(lambda acc, val: acc and None != re.match(block_quote_regex, val), splitted_block, True):
        return block_type_quote

    if reduce(lambda acc, val: acc and None != re.match(unordered_list_regex, val), splitted_block, True):
        return block_type_unordered_list
    
    if reduce(lambda acc, val: acc and None != re.match(ordered_list_regex, val), splitted_block, True):
        return block_type_ordered_list

    return block_type_paragraph
