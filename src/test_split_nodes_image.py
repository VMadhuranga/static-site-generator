import unittest

from textnode import TextNode
from split_nodes_image import split_nodes_image
from text_types import (
    text_type_text,
    text_type_image
)


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        # text with two images
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", text_type_text),
            TextNode(
                "image", 
                text_type_image, 
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
            ),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", 
                text_type_image, 
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ])

        # text with image at front 
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) This is text with an image at front",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode(
                "image", 
                text_type_image, 
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
            ),
            TextNode(" This is text with an image at front", text_type_text),
        ])

        # text with image at back
        node = TextNode(
            "This is text with an image at back ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image at back ", text_type_text),
            TextNode(
                "image", 
                text_type_image, 
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
            ),
        ])

        # text with image at middle
        node = TextNode(
            "This is text with an image ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) at middle",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image ", text_type_text),
            TextNode(
                "image", 
                text_type_image, 
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
            ),
            TextNode(" at middle", text_type_text),
        ])

        # text without images
        node = TextNode(
            "This is text with no image",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with no image", text_type_text),
        ])

        # text with a image 
        node = TextNode(
            "![With only image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("With only image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ])

        # text with empty image
        node = TextNode(
            "This is text with an empty image ![]() at middle",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an empty image ", text_type_text),
            TextNode(" at middle", text_type_text),
        ])

        # image without alt text
        node = TextNode(
            "This is text with an image without alt text ![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image without alt text ", text_type_text),
            TextNode("", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
        ])

        # image without url
        node = TextNode(
            "This is text with an image without url ![image]()",
            text_type_text
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image without url ", text_type_text),
            TextNode("image", text_type_image, ""),
        ])


if __name__ == "__main__":
    unittest.main()
