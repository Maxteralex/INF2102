import unittest
from unittest.mock import MagicMock
from mapper.definition_conn_mapper import DefinitionAccessMapper

class TestDefinitionAccessMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of DefinitionAccessMapper
        self.definition_access_mapper = DefinitionAccessMapper()
        self.definition_conn_config = {'connection_type': 'database'}

    def test_get_connection(self):
        # Test the getConnection method
        mock_definition_conn_class = MagicMock()
        mock_definition_conn_instance = MagicMock()
        mock_definition_conn_class.return_value = mock_definition_conn_instance
        self.definition_access_mapper._getKeyVariable = MagicMock(return_value=mock_definition_conn_class)

        result = self.definition_access_mapper.getConnection(self.definition_conn_config)

        self.assertEqual(result, mock_definition_conn_instance)
        mock_definition_conn_class.assert_called_once()
        mock_definition_conn_instance.configure.assert_called_once_with(self.definition_conn_config)

if __name__ == '__main__':
    unittest.main()
