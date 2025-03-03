import unittest
from unittest.mock import mock_open, patch

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

class TestReadFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='test data')
    def test_read_file(self, mock_file_open):
        # Call the function under test
        result = read_file('test.txt')
        
        # Check that the mock open function was called with the correct filename
        mock_file_open.assert_called_once_with('test.txt', 'r')
        
        # Check that the function returns the expected data
        self.assertEqual(result, 'test data')

if __name__ == '__main__':
    unittest.main()
