import os
import shutil


def copy_static_to_public(path_to_static, path_to_public):
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)

    os.mkdir(path_to_public)


    def copy_content(paths, previous_path):
        for path in paths:
            current_path = f"{previous_path}/{path}"

            if os.path.isfile(current_path):
                public_path = os.path.join(path_to_public, "/".join(current_path[len(f"{path_to_static}/"):].split("/")[:-1]))

                if not os.path.exists(public_path):
                    os.mkdir(public_path)

                shutil.copy(current_path, public_path)
            else:
                copy_content(os.listdir(current_path), current_path)

    copy_content(os.listdir(path_to_static), path_to_static)
