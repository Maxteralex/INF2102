import unittest
from unittest.mock import MagicMock
from mapper.load_conn_mapper import LoadConnectionMapper

class TestLoadConnectionMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of LoadConnectionMapper
        self.load_conn_mapper = LoadConnectionMapper()
        self.load_config = {'connection_type': 'database'}
        self.chunk_size = 10

    def test_get_connection(self):
        mock_load_conn_class = MagicMock()
        mock_load_conn_instance = MagicMock()
        mock_load_conn_class.return_value = mock_load_conn_instance
        self.load_conn_mapper._getKeyVariable = MagicMock(return_value=mock_load_conn_class)

        result = self.load_conn_mapper.getConnection(self.load_config, self.chunk_size)

        self.assertEqual(result, mock_load_conn_instance)
        mock_load_conn_class.assert_called_once()
        mock_load_conn_instance.configure.assert_called_once_with(self.load_config, self.chunk_size)

if __name__ == '__main__':
    unittest.main()
