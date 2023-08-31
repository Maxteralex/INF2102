import unittest
from unittest.mock import MagicMock
from mapper.model_queries_mapper import ModelQueriesMapper

class TestModelQueriesMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of ModelQueriesMapper
        self.model_queries_mapper = ModelQueriesMapper()
        self.analysis_timestamp = 1234567890

    def test_get_queries(self):
        # Test the getQueries method
        mock_model_queries_class = MagicMock()
        mock_model_queries_instance = MagicMock()
        mock_model_queries_class.return_value = mock_model_queries_instance
        self.model_queries_mapper._getKeyVariable = MagicMock(return_value=mock_model_queries_class)

        result = self.model_queries_mapper.getQueries('database', self.analysis_timestamp)

        self.assertEqual(result, mock_model_queries_instance)
        mock_model_queries_class.assert_called_once_with(self.analysis_timestamp)

if __name__ == '__main__':
    unittest.main()