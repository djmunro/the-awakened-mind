import os
import shutil

import jinja2
import markdown2
from jinja2 import Environment

SITE_DIR = 'SITE'
POSTS_DIR = 'posts'
TEMPLATES_DIR = '_templates'
TEMPLATE = 'template.html'
INDEX_TEMPLATE = 'index_template.html'


def post_links(posts):
    return [link for link in posts.keys()]


def build_index_page(posts, template):
    links = build_post_links(posts)
    html = render_template(template, {'posts': links})
    with open('{}/{}'.format(os.path.join(os.path.dirname(__file__), SITE_DIR), 'index.html'), 'w+') as file:
        file.write(html)


def render_template(template, context):
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), TEMPLATES_DIR))
    return Environment(loader=template_loader).get_template(template).render(context)


def build_post_links(posts):
    return [{'name': build_post_name(post), 'link': post} for post in posts]


def build_post_name(post):
    return post.split('.')[0].replace('-', ' ').capitalize()


def deploy_site():
    clean_site_directory(os.path.join(os.path.dirname(__file__), SITE_DIR))
    pages = build_post_pages(POSTS_DIR)
    write_pages(pages, directory=SITE_DIR)
    links = post_links(pages)
    build_index_page(links, INDEX_TEMPLATE)
    copy_css(['styles.css', 'normalize.css'], SITE_DIR)


def clean_site_directory(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        os.remove('{path}/{file}'.format(path=directory_path, file=file))


def build_post_pages(directory):
    posts = {}
    raw_posts = read_all_posts(directory=directory)
    for post in raw_posts:
        html = build_posts_from(post['content'], TEMPLATE)
        posts.update({'filename': '{}.html'.format(post['name']), 'html': html, 'header': post['header']})
    return posts


def build_posts_from(content, template):
    content = markdown2.markdown(content)
    return render_template(template, {'content': content})


def read_all_posts(directory):
    posts = []
    for file in get_all_file_paths(directory):
        header = extract_header(file)
        content = extract_content(file)
        posts.append({
            'name': clean_filename(file),
            'content': content,
            'header': header
        })
    return posts


def extract_header(file):
    content = read_file_content(file)
    data = content.split('---')[1].strip().split('\n')
    return list_to_dict(data)


def list_to_dict(rlist):
    return dict(map(lambda s: s.split(':'), rlist))


def extract_content(file):
    return read_file_content(file).split('---')[2].strip()


def write_pages(pages, directory):
    for page, content in pages.items():
        with open('{}/{}'.format(os.path.join(os.path.dirname(__file__), directory), page), 'w+') as file:
            file.write(content)


def copy_css(files, SITE_DIR):
    for file in files:
        shutil.copy(
            os.path.join(os.path.dirname(__file__), file),
            os.path.join(os.path.dirname(__file__), SITE_DIR)
        )


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
