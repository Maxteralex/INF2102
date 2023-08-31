import unittest
from unittest.mock import MagicMock
import pandas as pd
from connection.file_conn import FileConnection

class TestFileConnection(unittest.TestCase):

    def setUp(self):
        self.file_connection = FileConnection()

    def test_configure(self):
        # Test the configure method
        conn_settings = {'file_path': 'data.csv', 'file_separator': ','}
        chunk_size = 100
        self.file_connection.configure(conn_settings, chunk_size)
        self.assertEqual(self.file_connection.path, 'data.csv')
        self.assertEqual(self.file_connection.separator, ',')
        self.assertEqual(self.file_connection.chunk_size, chunk_size)

    def test_connect_csv(self):
        # Test the connect method with a CSV file
        self.file_connection.extension = 'csv'
        self.file_connection.path = 'data.csv'
        self.file_connection.connection_method = {'csv': pd.read_csv}
        self.file_connection.connect()
        self.assertIsNotNone(self.file_connection.conn)

    def test_disconnect(self):
        # Test the disconnect method
        self.file_connection.conn = MagicMock()
        self.file_connection.disconnect()
        self.assertIsNone(self.file_connection.conn)
        self.assertIsNone(self.file_connection.chunk)

    def test_next_chunk(self):
        # Test the nextChunk method
        mock_chunk = MagicMock()
        self.file_connection.chunk_size = None
        self.file_connection.conn = mock_chunk
        self.file_connection.nextChunk()
        self.assertEqual(self.file_connection.chunk, mock_chunk)

    def test_query(self):
        # Test the query method
        mock_chunk = MagicMock()
        self.file_connection.chunk = mock_chunk
        filters = ['column == 5']
        result = self.file_connection.query(filters, skiprows=0, nrows=100, order_by=['column'])
        self.assertEqual(result, mock_chunk.query.return_value[0:100].sort_values.return_value)

    def test_select_columns(self):
        # Test the selectColumns method
        mock_chunk = MagicMock()
        columns = ['col1', 'col2']
        self.file_connection.chunk = mock_chunk
        self.file_connection.selectColumns(columns)
        mock_chunk.__getitem__.assert_called_once_with(columns)

    def test_update(self):
        # Test the update method
        mock_chunk = MagicMock()
        self.file_connection.chunk = mock_chunk
        condition = 'column > 10'
        attribute = 'column'
        value = 5
        self.file_connection.update(condition, attribute, value)
        rows_to_update = mock_chunk.query.return_value.index
        mock_chunk.loc.assert_called_once_with(rows_to_update, attribute, value)

    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()
