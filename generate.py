import os


def get_all_file_paths(directory):
    file_names = os.listdir(os.path.join(os.path.dirname(__file__), directory))
    return [os.path.join(directory, file) for file in file_names]


def read_all_posts(directory):
    return {clean_filename(file): read_file_content(file) for file in get_all_file_paths(directory)}


def clean_filename(filepath):
    filename = remove_file_path_deatils(filepath)
    return convert_spaces_to_hyphens(filename)


def convert_spaces_to_hyphens(filename):
    return filename.replace(" ", "-")


def remove_file_path_deatils(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]


def read_file_content(filepath):
    path = os.path.join(os.path.dirname(__file__), filepath)
    with open(path, 'r') as file:
        return file.read()
