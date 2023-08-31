import unittest
from abc import abstractmethod
from pandas import DataFrame
from connection.load.load_access import LoadAccess

class TestLoadAccess(unittest.TestCase):

    def setUp(self):
        # Create a mock subclass of LoadAccess
        class MockLoadAccess(LoadAccess):
            @abstractmethod
            def initializeQueryConnection(self, query: dict) -> dict:
                pass

            @abstractmethod
            def getNextDataChunk(self) -> DataFrame:
                pass

        self.mock_load_access = MockLoadAccess()

    def test_abstract_methods(self):
        # Test that the abstract methods are defined
        with self.assertRaises(NotImplementedError):
            self.mock_load_access.initializeQueryConnection({})
        with self.assertRaises(NotImplementedError):
            self.mock_load_access.getNextDataChunk()

if __name__ == '__main__':
    unittest.main()
