import os

from markdown_to_html_node import mark_down_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    file = open(from_path)
    markdown = file.read()
    file.close()

    file = open(template_path)
    template = file.read()
    file.close()

    content = mark_down_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    file = open(dest_path, "w")
    file.write(template)
    file.close()
