import unittest
from model_queries.relational_database_queries import RelationalDatabaseQueries

class TestRelationalDatabaseQueries(unittest.TestCase):

    def setUp(self):
        # Create an instance of RelationalDatabaseQueries
        self.relational_database_queries = RelationalDatabaseQueries(1234567890)

    def test_sentiment_analysis_query(self):
        # Test the sentimentAnalysisQuery method
        result = self.relational_database_queries.sentimentAnalysisQuery()
        expected_result = {'query': 'SELECT id, text FROM post WHERE analysis = 1234567890'}
        self.assertEqual(result, expected_result)

    def test_toxic_analysis_query(self):
        # Test the toxicAnalysisQuery method
        result = self.relational_database_queries.toxicAnalysisQuery()
        expected_result = {'query': 'SELECT id, text FROM post WHERE analysis = 1234567890'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
