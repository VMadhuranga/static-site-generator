import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

```
def greet_person(name):
    print(f"hello, {name}")

greet_person()
```

* This is a list
* with items"""

        self.assertEqual(markdown_to_blocks(markdown), [
            "This is **bolded** paragraph", 
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", 
            "```\ndef greet_person(name):\n    print(f\"hello, {name}\")\n\ngreet_person()\n```", 
            "* This is a list\n* with items"
        ])

        # markdown with additional space character in empty line
        markdown = """This is **bolded** paragraph
     
Above empty line has some spaces
This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line
Below empty line has some spaces
             
* This is a list
* with items"""

        self.assertEqual(markdown_to_blocks(markdown), [
            "This is **bolded** paragraph", 
            "Above empty line has some spaces\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\nBelow empty line has some spaces", 
            "* This is a list\n* with items"
        ])

        # markdown with some blocks having leading and trailing white spaces
        markdown = """   This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line     

* This is a list
* with items      """

        self.assertEqual(markdown_to_blocks(markdown), [
            "This is **bolded** paragraph", 
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", 
            "* This is a list\n* with items"
        ])


if __name__ == "__main__":
    unittest.main()