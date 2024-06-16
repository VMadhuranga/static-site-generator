import unittest

from convert_paragraph import convert_paragraph


class TestConvertParagraph(unittest.TestCase):
    def test_convert_paragraph(self):
        paragraph = "This is a paragraph"
        self.assertEqual(convert_paragraph(paragraph).to_html(), "<p>This is a paragraph</p>")

        # paragraph with bold and italic words
        paragraph = "This is a paragraph with **bold** and *italic* words"
        self.assertEqual(convert_paragraph(paragraph).to_html(), "<p>This is a paragraph with <b>bold</b> and <i>italic</i> words</p>")

        # paragraph with bold and italic words and new line
        paragraph = """This is a paragraph with **bold** and *italic* words
This is the same paragraph on a new line"""
        self.assertEqual(convert_paragraph(paragraph).to_html(), "<p>This is a paragraph with <b>bold</b> and <i>italic</i> words<br />This is the same paragraph on a new line</p>")


if __name__ == "__main__":
    unittest.main()
