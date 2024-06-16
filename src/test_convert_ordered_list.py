import unittest

from convert_ordered_list import convert_ordered_list


class TestConvertOrderedList(unittest.TestCase):
    def test_convert_ordered_list(self):
        ordered_list = """1. item 1
2. item 2
3. item 3"""
        self.assertEqual(convert_ordered_list(ordered_list).to_html(), "<ol><li>item 1</li><li>item 2</li><li>item 3</li></ol>")

        # ordered list with italic word
        ordered_list = """1. item 1
2. *item* 2
3. item 3"""
        self.assertEqual(convert_ordered_list(ordered_list).to_html(), "<ol><li>item 1</li><li><i>item</i> 2</li><li>item 3</li></ol>")

        # ordered list with bold word
        ordered_list = """1. item 1
2. **item** 2
3. item 3"""
        self.assertEqual(convert_ordered_list(ordered_list).to_html(), "<ol><li>item 1</li><li><b>item</b> 2</li><li>item 3</li></ol>")


if __name__ == "__main__":
    unittest.main()
