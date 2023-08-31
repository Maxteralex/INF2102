import unittest
from unittest.mock import MagicMock
from mapper.save_conn_mapper import SaveConnectionMapper

class TestSaveConnectionMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of SaveConnectionMapper
        self.save_conn_mapper = SaveConnectionMapper()
        self.save_config = {'connection_type': 'database'}

    def test_get_connection(self):
        # Test the getConnection method
        mock_save_conn_class = MagicMock()
        mock_save_conn_instance = MagicMock()
        mock_save_conn_class.return_value = mock_save_conn_instance
        self.save_conn_mapper._getKeyVariable = MagicMock(return_value=mock_save_conn_class)

        result = self.save_conn_mapper.getConnection(self.save_config)

        self.assertEqual(result, mock_save_conn_instance)
        mock_save_conn_class.assert_called_once()
        mock_save_conn_instance.configure.assert_called_once_with(self.save_config)

if __name__ == '__main__':
    unittest.main()