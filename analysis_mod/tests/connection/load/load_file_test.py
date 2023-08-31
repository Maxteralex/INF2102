import unittest
from unittest.mock import MagicMock
from pandas import DataFrame
from connection.load.load_file import LoadFile

class TestLoadFile(unittest.TestCase):

    def setUp(self):
        # Create an instance of LoadFile
        self.load_file = LoadFile()
        self.load_file.connect = MagicMock()
        self.load_file.disconnect = MagicMock()
        self.load_file.nextChunk = MagicMock()
        self.load_file.query = MagicMock()
        self.load_file.selectColumns = MagicMock()
        self.load_file.getChunk = MagicMock(return_value=DataFrame({'col1': [1, 2], 'col2': [3, 4]}))

    def test_initialize_query_connection(self):
        # Test the initializeQueryConnection method
        query = {'columns': ['col1']}
        self.load_file.initializeQueryConnection(query)
        self.load_file.connect.assert_called_once()
        self.assertEqual(self.load_file.query_dict, query)

    def test_get_next_data_chunk(self):
        # Test the getNextDataChunk method
        query = {'columns': ['col1'], 'filters': ['col2 > 3']}
        self.load_file.query_dict = query
        result = self.load_file.getNextDataChunk()
        self.load_file.nextChunk.assert_called_once()
        self.load_file.query.assert_called_once_with(['col2 > 3'])
        self.load_file.selectColumns.assert_called_once_with(['col1'])
        self.assertEqual(result, self.load_file.query.return_value)

    def test_get_next_data_chunk_no_filters(self):
        # Test the getNextDataChunk method without filters
        query = {'columns': ['col1']}
        self.load_file.query_dict = query
        result = self.load_file.getNextDataChunk()
        self.load_file.nextChunk.assert_called_once()
        self.load_file.selectColumns.assert_called_once_with(['col1'])
        self.assertEqual(result, self.load_file.getChunk.return_value)

if __name__ == '__main__':
    unittest.main()
