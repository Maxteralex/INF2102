import unittest
from abc import abstractmethod
from connection.save.save_access import SaveAccess

class TestSaveAccess(unittest.TestCase):

    def setUp(self):
        # Create a mock subclass of SaveAccess
        class MockSaveAccess(SaveAccess):
            @abstractmethod
            def saveResults(self, results, query) -> None:
                pass

        self.mock_save_access = MockSaveAccess()

    def test_abstract_methods(self):
        # Test that the abstract methods are defined
        with self.assertRaises(NotImplementedError):
            self.mock_save_access.saveResults({}, {})

if __name__ == '__main__':
    unittest.main()