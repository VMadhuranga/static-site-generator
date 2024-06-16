import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "content", {"href": "http://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<a href=\"http://www.google.com\" target=\"_blank\">content</a>")

        # without value
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

        # without value ans empty string
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

        # without tag
        node = LeafNode(None, "content")
        self.assertEqual(node.to_html(), "content")

        # with tag as empty string
        node = LeafNode("", "content")
        self.assertEqual(node.to_html(), "content")

        # without props
        node = LeafNode("p", "content")
        self.assertEqual(node.to_html(), "<p>content</p>")

        # with props as empty dict
        node = LeafNode("p", "content", {})
        self.assertEqual(node.to_html(), "<p>content</p>")


if __name__ == "__main__":
    unittest.main()
