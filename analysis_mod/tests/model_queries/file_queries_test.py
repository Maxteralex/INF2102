import unittest
from model_queries.file_queries import FileQueries

class TestFileQueries(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileQueries
        self.file_queries = FileQueries(1234567890)

    def test_sentiment_analysis_query(self):
        # Test the sentimentAnalysisQuery method
        result = self.file_queries.sentimentAnalysisQuery()
        expected_result = {'filters': [], 'columns': ['id', 'text']}
        self.assertEqual(result, expected_result)

    def test_toxic_analysis_query(self):
        # Test the toxicAnalysisQuery method
        result = self.file_queries.toxicAnalysisQuery()
        expected_result = {'filters': [], 'columns': ['id', 'text']}
        self.assertEqual(result, expected_result)

    def test_sentiment_analysis_insert(self):
        # Test the sentimentAnalysisInsert method
        result = self.file_queries.sentimentAnalysisInsert()
        self.assertIsNone(result)

    def test_toxic_analysis_insert(self):
        # Test the toxicAnalysisInsert method
        result = self.file_queries.toxicAnalysisInsert()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
