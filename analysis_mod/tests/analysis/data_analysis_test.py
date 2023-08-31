import unittest
from unittest.mock import MagicMock
from analysis.data_analysis import DataAnalysis

class TestDataAnalysis(unittest.TestCase):

    def setUp(self):
        self.load_conn_mock = MagicMock()
        self.load_conn_mock.getConnection.return_value = 'mock_load_connection'
        self.save_conn_mock = MagicMock()
        self.save_conn_mock.getConnection.return_value = 'mock_save_connection'
        self.load_queries_mock = MagicMock()
        self.save_queries_mock = MagicMock()
        self.model_queries_mapper_mock = MagicMock()
        self.model_queries_mapper_mock.getQueries.side_effect = [
            self.load_queries_mock,
            self.save_queries_mock
        ]
        self.load_conn_mapper_mock = MagicMock()
        self.load_conn_mapper_mock.getConnection.return_value = self.load_conn_mock
        self.save_conn_mapper_mock = MagicMock()
        self.save_conn_mapper_mock.getConnection.return_value = self.save_conn_mock

        self.analysis_config = {
            'timestamp_created': 1234,
            'status': 'waiting',
            'load_config': {'connection_type': 'csv'},
            'save_config': {'connection_type': 'csv'}
        }

        self.data_analysis = DataAnalysis(self.analysis_config)
        self.data_analysis.load_conn_mapper = self.load_conn_mapper_mock
        self.data_analysis.save_conn_mapper = self.save_conn_mapper_mock
        self.data_analysis.model_queries_mapper = self.model_queries_mapper_mock

    def test_get_timestamp_created(self):
        timestamp = self.data_analysis.getTimestampCreated()
        self.assertEqual(timestamp, 1234)

    def test_init(self):
        self.assertEqual(self.data_analysis.timestamp_created, 1234)
        self.assertEqual(self.data_analysis.status, 'waiting')
        self.assertEqual(self.data_analysis.load_connection, 'mock_load_connection')
        self.assertEqual(self.data_analysis.load_queries, self.load_queries_mock)
        self.assertEqual(self.data_analysis.save_connection, 'mock_save_connection')
        self.assertEqual(self.data_analysis.save_queries, self.save_queries_mock)

    def test_process_abstract_method(self):
        with self.assertRaisesRegex(TypeError, "Can't instantiate abstract class"):
            self.data_analysis.process()

if __name__ == '__main__':
    unittest.main()
