import unittest

from textnode import (
    TextNode,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # test same properties
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        # test different "text" properties 
        node3 = TextNode("This is a text node 3", "bold")
        node4 = TextNode("This is a text node 4", "bold")
        self.assertNotEqual(node3, node4)

        # test different "text_type" properties 
        node5 = TextNode("This is a text node", "bold")
        node6 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node5, node6)
        
        # test different "url" properties 
        node7 = TextNode("This is a text node", "bold", "http://example.com")
        node8 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
