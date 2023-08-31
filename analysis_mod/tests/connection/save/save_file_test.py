import unittest
from unittest.mock import MagicMock
from pandas import DataFrame
from connection.save.save_file import SaveFile

class TestSaveFile(unittest.TestCase):

    def setUp(self):
        # Create an instance of SaveFile
        self.save_file = SaveFile()
        self.save_file.saveFile = MagicMock()
        self.save_file.disconnect = MagicMock()
        self.save_file.connect = MagicMock()

    def test_save_results(self):
        # Test the saveResults method
        results = DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        query = {}
        self.save_file.saveResults(results, query)
        self.save_file._setConnection.assert_called_once_with(results)
        self.save_file.saveFile.assert_called_once_with(partial=True)
        self.save_file.disconnect.assert_called_once()

    def test_set_connection(self):
        # Test the _setConnection method
        connection = DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        self.save_file._setConnection(connection)
        self.assertEqual(self.save_file.conn, connection)
        self.assertEqual(self.save_file.chunk, connection)
        self.assertEqual(self.save_file.chunk_index, 0)

if __name__ == '__main__':
    unittest.main()
