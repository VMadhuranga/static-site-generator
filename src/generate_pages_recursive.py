import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    def generate(paths, previous_path):
        for path in paths:
            current_path = f"{previous_path}/{path}"

            if os.path.isfile(current_path):
                dest_path = os.path.join(dest_dir_path, current_path[len(f"{dir_path_content}/"):]).replace(".md", ".html")
                generate_page(current_path, template_path, dest_path)
            else:
                generate(os.listdir(current_path), current_path)

    generate(os.listdir(dir_path_content), dir_path_content)
