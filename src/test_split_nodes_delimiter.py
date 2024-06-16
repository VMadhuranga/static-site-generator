import unittest

from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from text_types import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        # text with code block
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ])

        # text with bold word
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

        node = TextNode("This is text with a __bold__ word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "__", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

        # text with italic word
        node = TextNode("This is text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ])

        node = TextNode("This is text with a _italic_ word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "_", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ])

        # with different text_type 
        node = TextNode("*This is a italic word*", text_type_italic)
        node2 = TextNode("**This is a bold word**", text_type_bold)
        new_nodes = split_nodes_delimiter([node, node2], "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("*This is a italic word*", text_type_italic),
            TextNode("**This is a bold word**", text_type_bold)
        ])

        # without closing delimiter
        node = TextNode("This is text with a *italic word without closing delimiter", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", text_type_italic)

        node = TextNode("This is text with two *italic* words *italic2*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This is text with two ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" words ", text_type_text),
            TextNode("italic2", text_type_italic)
        ])

        # text with italic word at last
        node = TextNode("This is text with a italic word at last *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a italic word at last ", text_type_text),
            TextNode("italic", text_type_italic)
        ])

        # text with italic word at first
        node = TextNode("*italic* This is text with a italic word at first", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(new_nodes, [
            TextNode("italic", text_type_italic),
            TextNode(" This is text with a italic word at first", text_type_text)
        ])


if __name__ == "__main__":
    unittest.main()
