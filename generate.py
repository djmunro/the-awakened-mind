import os
import shutil

import jinja2
import markdown2
from jinja2 import Environment

SITE_DIR = 'SITE'
POSTS_DIR = 'posts'
TEMPLATE = 'template.html'


def deploy_site():
    clean_site_directory(os.path.join(os.path.dirname(__file__), SITE_DIR))
    pages = build_post_pages(POSTS_DIR)
    write_pages(pages, directory=SITE_DIR)
    copy_css('styles.css', SITE_DIR)


def clean_site_directory(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        os.remove('{path}/{file}'.format(path=directory_path, file=file))


def build_post_pages(directory):
    posts = {}
    raw_posts = read_all_posts(directory=directory)
    for filename, content in raw_posts.items():
        content = markdown2.markdown(content)
        template_loader = jinja2.FileSystemLoader(searchpath=os.path.dirname(__file__))
        html = Environment(loader=template_loader).get_template(TEMPLATE).render(content=content)
        posts.update({'{}.html'.format(filename): html})
    return posts


def write_pages(pages, directory):
    for page, content in pages.items():
        with open('{}/{}'.format(os.path.join(os.path.dirname(__file__), directory), page), 'w+') as file:
            file.write(content)


def copy_css(css_file, SITE_DIR):
    return shutil.copy(
        os.path.join(os.path.dirname(__file__), css_file),
        os.path.join(os.path.dirname(__file__), SITE_DIR)
    )


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


if __name__ == '__main__':
    deploy_site()
