import unittest

from convert_heading import convert_heading
from parentnode import ParentNode
from leafnode import LeafNode


class TestConvertHeading(unittest.TestCase):
    def test_convert_heading(self):
        h1 = "# heading 1"
        h2 = "## heading 2"
        h3 = "### heading 3"
        h4 = "#### heading 4"
        h5 = "##### heading 5"
        h6 = "###### heading 6"

        self.assertEqual(convert_heading(h1).to_html(), "<h1>heading 1</h1>")
        self.assertEqual(convert_heading(h2).to_html(), "<h2>heading 2</h2>")
        self.assertEqual(convert_heading(h3).to_html(), "<h3>heading 3</h3>")
        self.assertEqual(convert_heading(h4).to_html(), "<h4>heading 4</h4>")
        self.assertEqual(convert_heading(h5).to_html(), "<h5>heading 5</h5>")
        self.assertEqual(convert_heading(h6).to_html(), "<h6>heading 6</h6>")

        # empty heading
        with self.assertRaises(ValueError):
            convert_heading("# ").to_html()

        # heading italic word
        heading = "### *heading* level 3"
        self.assertEqual(convert_heading(heading).to_html(), "<h3><i>heading</i> level 3</h3>")


if __name__ == "__main__":
    unittest.main()