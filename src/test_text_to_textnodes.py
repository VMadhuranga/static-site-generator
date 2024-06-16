import unittest

from textnode import TextNode
from text_to_textnodes import text_to_textnodes
from text_types import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        # text with bold, italic words and code block, image and link
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ])

        # text without bold, italic words and code block, image and link
        text = "This is normal text"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is normal text", text_type_text),
        ])

        # text with bold word
        text = "This is text with a **bold** word"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

        text = "This is text with a __bold__ word"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ])

        # text with italic word
        text = "This is text with an *italic* word"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ])

        text = "This is text with an _italic_ word"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ])

        # text with code block
        text = "This is text with a `code block`"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
        ])

        # text with image
        text = "This is text a ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text a ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ])

        # text with link
        text = "This is text with a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ])


if __name__ == "__main__":
    unittest.main()
