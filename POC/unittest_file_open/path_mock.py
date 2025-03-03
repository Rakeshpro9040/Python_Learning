import unittest
from unittest.mock import patch
from pathlib import Path

def check_path_existence(path):
    if Path(path).exists():
        return True
    else:
        return False

class TestCheckPathExistence(unittest.TestCase):
    @patch('pathlib.Path.exists', return_value=True)
    def test_existing_path(self, mock_exists):
        result = check_path_existence('/path/to/existing/file.txt')
        self.assertTrue(result)

    @patch('pathlib.Path.exists', return_value=False)
    def test_non_existing_path(self, mock_exists):
        result = check_path_existence('/path/to/non/existing/file.txt')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
