import unittest
from unittest.mock import MagicMock
from analysis.sentiment_analysis import SentimentAnalysis
import pandas as pd

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        self.load_conn_mock = MagicMock()
        self.save_conn_mock = MagicMock()
        self.load_queries_mock = MagicMock()
        self.save_queries_mock = MagicMock()
        self.model_queries_mapper_mock = MagicMock()
        self.model_queries_mapper_mock.getQueries.side_effect = [
            self.load_queries_mock,
            self.save_queries_mock
        ]

        self.sentiment_analysis = SentimentAnalysis({})
        self.sentiment_analysis.load_connection = self.load_conn_mock
        self.sentiment_analysis.save_connection = self.save_conn_mock
        self.sentiment_analysis.load_queries = self.load_queries_mock
        self.sentiment_analysis.save_queries = self.save_queries_mock

    def test_classify(self):
        data_chunk = pd.DataFrame({
            'id': [1, 2, 3],
            'text': ['positive text', 'neutral text', 'negative text']
        })
        mock_response = {'classification': ['positive', 'neutral', 'negative']}
        mock_post = MagicMock()
        mock_post.json.return_value = mock_response
        with unittest.mock.patch('requests.post', return_value=mock_post):
            result_df = self.sentiment_analysis.classify(data_chunk)
        expected_df = pd.DataFrame({
            'id': [1, 2, 3],
            'classification': ['positive', 'neutral', 'negative']
        })
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_process(self):
        self.load_conn_mock.initializeQueryConnection.return_value = None
        self.load_conn_mock.getNextDataChunk.side_effect = [
            pd.DataFrame({'id': [1, 2]}), None
        ]
        mock_results = pd.DataFrame({'id': [1, 2], 'classification': ['positive', 'neutral']})
        with unittest.mock.patch.object(
            self.sentiment_analysis, 'classify', return_value=mock_results
        ):
            self.sentiment_analysis.process()
        self.assertEqual(self.load_conn_mock.initializeQueryConnection.call_count, 1)
        self.assertEqual(self.load_conn_mock.getNextDataChunk.call_count, 2)
        self.assertEqual(self.save_conn_mock.saveResults.call_count, 1)
        self.assertEqual(self.save_conn_mock.saveResults.call_args[0][0], mock_results)
        self.assertEqual(self.save_conn_mock.saveResults.call_args[0][1], self.save_queries_mock.sentimentAnalysisInsert())

if __name__ == '__main__':
    unittest.main()