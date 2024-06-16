import unittest

from textnode import TextNode
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHtml(unittest.TestCase):
    def test_text_node_to_html_node(self):
        # text type = text
        node = TextNode("content", "text")
        self.assertEqual(text_node_to_html_node(node).to_html(), "content")

        # text type = bold
        node = TextNode("content", "bold")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>content</b>")

        # text type = italic
        node = TextNode("content", "italic")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<i>content</i>")

        # text type = code
        node = TextNode("content", "code")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<code>content</code>")

        # text type = link
        node = TextNode("content", "link", "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<a href=\"https://www.google.com\">content</a>")

        # text type = text
        node = TextNode("some image", "image", "https://some.image.url")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<img src=\"https://some.image.url\" alt=\"some image\"></img>")

        # text type = invalid type
        node = TextNode("some image", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node).to_html()


if __name__ == "__main__":
    unittest.main()
