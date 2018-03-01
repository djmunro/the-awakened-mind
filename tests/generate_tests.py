import unittest

from generate import read_all_posts, get_all_file_paths


class GenerateTests(unittest.TestCase):

    def test_read_all_posts(self):
        posts = read_all_posts(directory='posts')
        self.assertTrue(len(posts) >= 1)

    def test_get_all_file_paths_are_valid(self):
        file_paths = get_all_file_paths(directory='posts')
        self.assertEqual(file_paths[0], 'posts/test-post.md')
