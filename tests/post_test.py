import unittest

from post import Post


class PostTests(unittest.TestCase):

    @staticmethod
    def post_content():
        return '''
        ---
        title: Why the minimal-blog is there?
        foo: bar
        ---
        
        Name of the post
        '''

    def test_get_post_headers(self):
        self.assertEqual({'title': 'Why the minimal-blog is there?', 'foo': 'bar'}, Post(self.post_content()).headers)

    def test_get_post_content(self):
        self.assertEqual('Name of the post', Post(self.post_content()).content)
