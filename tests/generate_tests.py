import os
import unittest

import markdown2
from jinja2 import Environment

from generate import read_all_posts, get_all_file_paths, clean_filename, clean_site_directory, SITE_DIR


class GenerateTests(unittest.TestCase):

    def test_read_all_posts(self):
        posts = read_all_posts(directory='posts')
        self.assertEqual({'test-post':'Name of the post'}, posts)

    def test_get_all_file_paths_are_valid(self):
        file_paths = get_all_file_paths(directory='posts')
        self.assertEqual('posts/test-post.md', file_paths[0])

    def test_clean_filename(self):
        cleaned_name = clean_filename('posts/test-post.md')
        self.assertEqual('test-post', cleaned_name)

    def test_clean_filename_when_file_has_spaces(self):
        cleaned_name = clean_filename('posts/test post.md')
        self.assertEqual('test-post', cleaned_name)

    def test_delete(self):
        # TODO temp dir
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        open("{}/{}/test.file".format(parent_dir, SITE_DIR), "w+")
        clean_site_directory(os.path.join(parent_dir, SITE_DIR))

    def test_rendering_template(self):
        template = '''
        <!DOCTYPE html>
        <html>
            <body>
                {{content}}
            </body>
        </html>
        '''
        expected_html = '''
        <!DOCTYPE html>
        <html>
            <body>
                Test content
            </body>
        </html>
        '''
        html = Environment().from_string(template).render(content='Test content')
        self.assertEqual(expected_html, html)

    def test_markdown_converter(self):
        html_from_md = markdown2.markdown("*boo!*")
        expected_html = '<p><em>boo!</em></p>\n'
        self.assertEqual(expected_html, html_from_md)
