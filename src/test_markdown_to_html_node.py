import unittest

from markdown_to_html_node import mark_down_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """# This is a heading level 1

## This is a heading level 2

### This is a heading level 3

#### This is a heading level 4

##### This is a heading level 5

###### This is a heading level 6

This is a paragraph with **bold** and *italic* words
This is the same paragraph on the new line with [link](https://www.google.com)

* unordered list item 1
* unordered list item 2
* unordered list item 3
* unordered list item 4

- unordered list item 1
- unordered list item 2
- unordered list item 3
- unordered list item 4

1. ordered list item 1
2. ordered list item 2
3. ordered list item 3
4. ordered list item 4

```
def greet_person(name):
    print(f"Hello, {name}")

greet_person("john")
```

> This is a block quote with **bold** word

> This is a block quote with *italic* word"""
        self.assertEqual(mark_down_to_html_node(markdown).to_html(), "<div><h1>This is a heading level 1</h1><h2>This is a heading level 2</h2><h3>This is a heading level 3</h3><h4>This is a heading level 4</h4><h5>This is a heading level 5</h5><h6>This is a heading level 6</h6><p>This is a paragraph with <b>bold</b> and <i>italic</i> words<br />This is the same paragraph on the new line with <a href=\"https://www.google.com\">link</a></p><ul><li>unordered list item 1</li><li>unordered list item 2</li><li>unordered list item 3</li><li>unordered list item 4</li></ul><ul><li>unordered list item 1</li><li>unordered list item 2</li><li>unordered list item 3</li><li>unordered list item 4</li></ul><ol><li>ordered list item 1</li><li>ordered list item 2</li><li>ordered list item 3</li><li>ordered list item 4</li></ol><code><pre>def greet_person(name):&NewLine;    print(f\"Hello, {name}\")&NewLine;&NewLine;greet_person(\"john\")</pre></code><blockquote>This is a block quote with <b>bold</b> word</blockquote><blockquote>This is a block quote with <i>italic</i> word</blockquote></div>")

        # markdown with spaces
        markdown = """



# This is a heading level 1



This is a paragraph with **bold** and *italic* words
This is the same paragraph on the new line with [link](https://www.google.com)



* unordered list item 1
* unordered list item 2



- unordered list item 1
- unordered list item 2



1. ordered list item 1
2. ordered list item 2



```
def greet_person(name):
    print(f"Hello, {name}")

greet_person("john")
```


> This is a block quote with **bold** word



> This is a block quote with *italic* word



"""
        self.assertEqual(mark_down_to_html_node(markdown).to_html(), "<div><h1>This is a heading level 1</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> words<br />This is the same paragraph on the new line with <a href=\"https://www.google.com\">link</a></p><ul><li>unordered list item 1</li><li>unordered list item 2</li></ul><ul><li>unordered list item 1</li><li>unordered list item 2</li></ul><ol><li>ordered list item 1</li><li>ordered list item 2</li></ol><code><pre>def greet_person(name):&NewLine;    print(f\"Hello, {name}\")&NewLine;&NewLine;greet_person(\"john\")</pre></code><blockquote>This is a block quote with <b>bold</b> word</blockquote><blockquote>This is a block quote with <i>italic</i> word</blockquote></div>")


if __name__ == "__main__":
    unittest.main()