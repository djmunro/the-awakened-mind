import os
import unittest

from generate import get_files, clean_filename
from old.generate import get_all_file_paths


class GenerateTests(unittest.TestCase):

    def test_get_files(self):
        self.assertTrue(len(get_files(os.path.join(os.path.dirname(__file__), '../_posts'))) == 1)

    def test_get_all_file_paths_are_valid(self):
        file_paths = get_all_file_paths(directory='posts')
        self.assertEqual('posts/test-post.md', file_paths[0])

    def test_clean_filename(self):
        cleaned_name = clean_filename('posts/test-post.md')
        self.assertEqual('test-post', cleaned_name)

    def test_clean_filename_when_file_has_spaces(self):
        cleaned_name = clean_filename('posts/test post.md')
        self.assertEqual('test-post', cleaned_name)

