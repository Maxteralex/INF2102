import unittest
from abc import abstractmethod
from model_queries.model_queries import ModelQueries

class TestModelQueries(unittest.TestCase):

    def setUp(self):
        # Create a mock subclass of ModelQueries
        class MockModelQueries(ModelQueries):
            @abstractmethod
            def sentimentAnalysisQuery(self) -> dict:
                pass

            @abstractmethod
            def toxicAnalysisQuery(self) -> dict:
                pass

            @abstractmethod
            def sentimentAnalysisInsert(self) -> dict:
                pass

        self.mock_model_queries = MockModelQueries(1234567890)

    def test_abstract_methods(self):
        # Test that the abstract methods are defined
        with self.assertRaisesRegex(TypeError, "Can't instantiate abstract class"):
            ModelQueries(1234567890)
        with self.assertRaises(NotImplementedError):
            self.mock_model_queries.sentimentAnalysisQuery()
        with self.assertRaises(NotImplementedError):
            self.mock_model_queries.toxicAnalysisQuery()
        with self.assertRaises(NotImplementedError):
            self.mock_model_queries.sentimentAnalysisInsert()

if __name__ == '__main__':
    unittest.main()
