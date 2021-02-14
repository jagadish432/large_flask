import json
import os


def get_json_from_file(filename, my_path):
    file_content = read_local_file(filename, my_path)
    response = json.loads(file_content)
    return response


def read_local_file(relative_path_filename, my_path):
    path = os.path.join(my_path, relative_path_filename)
    with open(path) as f:
        return f.read()