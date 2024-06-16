from copy_static_to_public import copy_static_to_public
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def main():
    copy_static_to_public("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()
