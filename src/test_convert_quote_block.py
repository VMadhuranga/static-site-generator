import unittest

from convert_quote_block import convert_quote_block


class TestConvertQuoteBlock(unittest.TestCase):
    def test_convert_quote_block(self):
        quote_block = "> This is quote block"
        self.assertEqual(convert_quote_block(quote_block).to_html(), "<blockquote>This is quote block</blockquote>")

        quote_block = ">   This is quote block"
        self.assertEqual(convert_quote_block(quote_block).to_html(), "<blockquote>This is quote block</blockquote>")

        # empty quote block
        quote_block = ">  "
        with self.assertRaises(ValueError):
            convert_quote_block(quote_block).to_html()

        # quote block with bold text
        quote_block = "> This is **quote** block"
        self.assertEqual(convert_quote_block(quote_block).to_html(), "<blockquote>This is <b>quote</b> block</blockquote>")

        # multiline quote block
        quote_block = """> This is **quote** block
> This is a *quote* block on new line"""
        self.assertEqual(convert_quote_block(quote_block).to_html(), "<blockquote>This is <b>quote</b> block This is a <i>quote</i> block on new line</blockquote>")

if __name__ == "__main__":
    unittest.main()
