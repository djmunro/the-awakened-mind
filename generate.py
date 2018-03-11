import os
import shutil

from post import Post
from post_html_generator import PostHtmlGenerator

SITE_DIR = 'SITE'


def deploy_site():
    generate_posts()
    copy_css(['styles.css', 'normalize.css'], SITE_DIR)


def generate_posts():
    files = get_files(os.path.join(os.path.dirname(__file__), '_posts'))
    for file in files:
        post = build_post(file)
        filename = clean_filename(file)
        write_post(filename, post, 'SITE')


def get_files(directory):
    file_names = os.listdir(os.path.join(os.path.dirname(__file__), directory))
    return [os.path.join(directory, file) for file in file_names]


def build_post(file):
    content = read_file_content(file)
    post = Post(content)
    return PostHtmlGenerator(post).render_template('template.html')


def read_file_content(filepath):
    path = os.path.join(os.path.dirname(__file__), filepath)
    with open(path, 'r') as file:
        return file.read()


def clean_filename(filepath):
    filename = remove_file_path_deatils(filepath)
    return convert_spaces_to_hyphens(filename)


def remove_file_path_deatils(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]


def convert_spaces_to_hyphens(filename):
    return filename.replace(" ", "-")


def write_post(post_name, content, directory):
    with open('{}/{}.html'.format(os.path.join(os.path.dirname(__file__), directory), post_name), 'w+') as file:
        file.write(content)


def copy_css(files, directory):
    for file in files:
        shutil.copy(
            os.path.join(os.path.dirname(__file__), file),
            os.path.join(os.path.dirname(__file__), directory)
        )


if __name__ == '__main__':
    deploy_site()
