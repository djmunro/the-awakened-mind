import unittest

from generate import read_all_posts, get_all_file_paths, clean_filename


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

