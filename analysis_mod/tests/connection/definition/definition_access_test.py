import unittest
from abc import abstractmethod
from connection.definition.definition_access import DefinitionAccess

class TestDefinitionAccess(unittest.TestCase):

    def setUp(self):
        # Create a mock subclass of DefinitionAccess
        class MockDefinitionAccess(DefinitionAccess):
            @abstractmethod
            def getNextScheduledAnalysisConfiguration(self) -> dict:
                pass

            @abstractmethod
            def updateAnalysisStatus(self, analysis_timestamp: int) -> None:
                pass

        self.mock_definition_access = MockDefinitionAccess()

    def test_abstract_methods(self):
        # Test that the abstract methods are defined
        with self.assertRaises(NotImplementedError):
            self.mock_definition_access.getNextScheduledAnalysisConfiguration()
        with self.assertRaises(NotImplementedError):
            self.mock_definition_access.updateAnalysisStatus(1234567890)

if __name__ == '__main__':
    unittest.main()
