import os

SITE_DIR = 'SITE'


def deploy_site(posts):
    clean_site_directory(os.path.join(os.path.dirname(__file__), SITE_DIR))
    pages = build_post_pages(posts)
    write_pages(pages, directory=SITE_DIR)


def clean_site_directory(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        os.remove('{path}/{file}'.format(path=directory_path, file=file))


def build_post_pages(posts):
    pass


def write_pages(pages, directory):
    pass


def read_all_posts(directory):
    return {clean_filename(file): read_file_content(file) for file in get_all_file_paths(directory)}


def get_all_file_paths(directory):
    file_names = os.listdir(os.path.join(os.path.dirname(__file__), directory))
    return [os.path.join(directory, file) for file in file_names]


def clean_filename(filepath):
    filename = remove_file_path_deatils(filepath)
    return convert_spaces_to_hyphens(filename)


def read_file_content(filepath):
    path = os.path.join(os.path.dirname(__file__), filepath)
    with open(path, 'r') as file:
        return file.read()


def remove_file_path_deatils(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]


def convert_spaces_to_hyphens(filename):
    return filename.replace(" ", "-")
