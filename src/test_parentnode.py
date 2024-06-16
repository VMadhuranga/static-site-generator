import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        # parent node with multiple children nodes
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        # parent node with parent node inside
        node = ParentNode(
            "nav",
            [
                ParentNode("ul", [
                    LeafNode("li", "Home"),
                    LeafNode("li", "About"),
                    LeafNode("li", "Contact")
                ]),
            ],
        )
        self.assertEqual(node.to_html(), "<nav><ul><li>Home</li><li>About</li><li>Contact</li></ul></nav>")

        # without tag
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

        # with tag as empty string
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

        # with tag as empty string in child parent
        node = ParentNode(
            "nav",
            [
                ParentNode("", [
                    LeafNode("li", "Home"),
                    LeafNode("li", "About"),
                    LeafNode("li", "Contact")
                ]),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

        # without children
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

        # with children an empty list
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()

        # with children an empty list in parent node
        node = ParentNode(
            "nav",
            [
                ParentNode("ul", []),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
