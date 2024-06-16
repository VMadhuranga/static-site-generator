import unittest

from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from block_types import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        # headings
        markdown = """# heading 1

        ## heading 2

        ### heading 3

        #### heading 4

        ##### heading 5

        ###### heading 6"""

        headings = markdown_to_blocks(markdown)

        self.assertEqual(block_to_block_type(headings[0]), block_type_heading)
        self.assertEqual(block_to_block_type(headings[1]), block_type_heading)
        self.assertEqual(block_to_block_type(headings[2]), block_type_heading)
        self.assertEqual(block_to_block_type(headings[3]), block_type_heading)
        self.assertEqual(block_to_block_type(headings[4]), block_type_heading)
        self.assertEqual(block_to_block_type(headings[5]), block_type_heading)

        # empty heading
        markdown = """#"""
        self.assertEqual(block_to_block_type(headings[0]), block_type_heading)

        # code blocks
        markdown = """```
        print("hello")
        ```"""
        code_block = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(code_block), block_type_code)

        markdown = """```print("hello")```"""
        code_block = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(code_block), block_type_code)

        # empty code block
        markdown = """```
```"""
        code_block = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(code_block), block_type_code)

        # empty code block with empty new line
        markdown = """```

```"""
        code_block = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(code_block), block_type_code)

        # block quotes
        markdown = "> block quote"
        block_quote = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(block_quote), block_type_quote)

        markdown = ">block quote"
        block_quote = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(block_quote), block_type_paragraph)

        markdown = ">   block quote"
        block_quote = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(block_quote), block_type_quote)

        # empty block quote
        markdown = ">"
        block_quote = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(block_quote), block_type_paragraph)

        # unordered lists
        markdown = """* item one
        * item two"""
        unordered_list = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(unordered_list), block_type_unordered_list)

        markdown = """- item one
        - item two"""
        unordered_list = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(unordered_list), block_type_unordered_list)

        # empty unordered list
        markdown = """- 
        - """
        unordered_list = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(unordered_list), block_type_paragraph)

        # ordered list
        markdown = """1. item one
        2. item two"""
        ordered_list = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(ordered_list), block_type_ordered_list)
        
        # paragraph
        markdown = """This is another paragraph
        This is the same paragraph on a new line"""
        paragraph = markdown_to_blocks(markdown)[0]
        self.assertEqual(block_to_block_type(paragraph), block_type_paragraph)
        

if __name__ == "__main__":
    unittest.main()
