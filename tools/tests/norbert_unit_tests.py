import sys
sys.path.append("../../")
import os
import shutil
import unittest
from mock import patch, MagicMock
import playgame


class norbert_unit_tests(unittest.TestCase):
    def setUp(self):
        os.makedirs("results/")
    
    def tearDown(self):
        shutil.rmtree("results/") 

    def test_empy_dirname(self):
        self.assertEqual(playgame.isdir(""), True)
        
    def test_dir_not_exits(self):
        self.assertEqual(playgame.isdir("directory/that/does/not/exits"), False)

    def test_dir_exists(self):
        self.assertEqual(playgame.isdir("results/"), True)

    def test_make_directory(self):
        file_path="results/a/b/c/results.txt"
        dir_name="results/a/b/c"
        playgame.ensure_path(file_path)
        self.assertEqual(os.path.isdir(dir_name),True)
        
    @patch('playgame.isdir')
    def test_is_called_ensure_path(self, mock):
        path = "results/path/test"
        playgame.ensure_path(path)
        mock.assert_called_once_with(os.path.dirname(path))


if __name__ == '__main__':
    unittest.main()
