import unittest

from post import Post
from post_html_generator import PostHtmlGenerator


class PostHtmlGeneratorTest(unittest.TestCase):

    @staticmethod
    def post_content():
        return '''
            ---
            title: Why the minimal-blog is there?
            foo: bar
            ---

            Name of the post
            '''

    def test_generate_html(self):
        self.assertTrue(PostHtmlGenerator(Post(self.post_content())).render_template('template.html'))
