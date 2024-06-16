import unittest 

from convert_code_block import convert_code_block


class TestConvertCodeBlock(unittest.TestCase):
    def test_convert_code_block(self):
        code_block = """```
def greet_person(name):
    print(f"hello, {name}")
```"""
        self.assertEqual(convert_code_block(code_block).to_html(), "<pre><code>def greet_person(name):&NewLine;    print(f\"hello, {name}\")</code></pre>")

        code_block = """```
def greet_person(name):
    return f"hello, {name}"

print(greet_person("John"))
```"""
        self.assertEqual(convert_code_block(code_block).to_html(), "<pre><code>def greet_person(name):&NewLine;    return f\"hello, {name}\"&NewLine;&NewLine;print(greet_person(\"John\"))</code></pre>")

        code_block = """```
print("hello")
```"""
        self.assertEqual(convert_code_block(code_block).to_html(), "<pre><code>print(\"hello\")</code></pre>")

        # empty code block
        code_block = """```
```"""
        with self.assertRaises(ValueError):
            convert_code_block(code_block).to_html()



if __name__ == "__main__":
    unittest.main()
