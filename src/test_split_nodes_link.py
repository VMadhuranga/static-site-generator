import unittest

from textnode import TextNode
from split_nodes_link import split_nodes_link
from text_types import (
    text_type_text,
    text_type_link
)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        # text with two links
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.example.com)",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode(
                "link", 
                text_type_link, 
                "https://www.google.com"
            ),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", 
                text_type_link, 
                "https://www.example.com"
            ),
        ])

        # text with link at front 
        node = TextNode(
            "[link](https://www.google.com) This is text with a link at front",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode(
                "link", 
                text_type_link, 
                "https://www.google.com"
            ),
            TextNode(" This is text with a link at front", text_type_text),
        ])

        # text with link at back
        node = TextNode(
            "This is text with a link at back [link](https://www.google.com)",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link at back ", text_type_text),
            TextNode(
                "link", 
                text_type_link, 
                "https://www.google.com"
            ),
        ])

        # text with link at middle
        node = TextNode(
            "This is text with a link [link](https://www.google.com) at middle",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link ", text_type_text),
            TextNode(
                "link", 
                text_type_link, 
                "https://www.google.com"
            ),
            TextNode(" at middle", text_type_text),
        ])

        # text without links
        node = TextNode(
            "This is a text with no links",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is a text with no links", text_type_text),
        ])

        # text with a link 
        node = TextNode(
            "[With only link](https://www.google.com)",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("With only link", text_type_link, "https://www.google.com"),
        ])

        # text with empty link
        node = TextNode(
            "This is text with a empty link []() at middle",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a empty link ", text_type_text),
            TextNode(" at middle", text_type_text),
        ])

        # link without link text
        node = TextNode(
            "This is text with a link without link text [](https://www.google.com)",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link without link text ", text_type_text),
            TextNode("", text_type_link, "https://www.google.com"),
        ])

        # link without url
        node = TextNode(
            "This is text with a link without url [image]()",
            text_type_text
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link without url ", text_type_text),
            TextNode("image", text_type_link, ""),
        ])


if __name__ == "__main__":
    unittest.main()
