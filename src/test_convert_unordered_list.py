import unittest

from convert_unordered_list import convert_unordered_list


class TestConvertUnorderedList(unittest.TestCase):
    def test_convert_unordered_list(self):
        unordered_list = """* item 1
* item 2
* item 3"""
        self.assertEqual(convert_unordered_list(unordered_list).to_html(), "<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>")

        unordered_list = """- item 1
- item 2
- item 3"""
        self.assertEqual(convert_unordered_list(unordered_list).to_html(), "<ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>")

        # unordered list with bold word
        unordered_list = """* item 1
* *item* 2
* item 3"""
        self.assertEqual(convert_unordered_list(unordered_list).to_html(), "<ul><li>item 1</li><li><i>item</i> 2</li><li>item 3</li></ul>")

        # unordered list with bold word
        unordered_list = """- item 1
- **item** 2
- item 3"""
        self.assertEqual(convert_unordered_list(unordered_list).to_html(), "<ul><li>item 1</li><li><b>item</b> 2</li><li>item 3</li></ul>")


if __name__ == "__main__":
    unittest.main()
