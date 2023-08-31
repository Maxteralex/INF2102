import unittest
from unittest.mock import MagicMock
from connection.definition.definition_file import DefinitionFile
import pandas as pd

class TestDefinitionFile(unittest.TestCase):

    def setUp(self):
        # Create an instance of DefinitionFile
        self.definition_file = DefinitionFile()

    def test_get_next_scheduled_analysis_configuration(self):
        # Test the getNextScheduledAnalysisConfiguration method
        self.definition_file.connect = MagicMock()
        self.definition_file.disconnect = MagicMock()
        self.definition_file.nextChunk = MagicMock()
        self.definition_file.query = MagicMock(return_value=pd.DataFrame({'status': ['waiting'], 'timestamp_created': [1234567890]}))
        
        result = self.definition_file.getNextScheduledAnalysisConfiguration()
        
        self.assertEqual(result, {'status': 'waiting', 'timestamp_created': 1234567890})
        self.definition_file.connect.assert_called_once()
        self.definition_file.disconnect.assert_called_once()
        self.definition_file.nextChunk.assert_called_once()
        self.definition_file.query.assert_called_once()

    def test_update_analysis_status(self):
        # Test the updateAnalysisStatus method
        self.definition_file.connect = MagicMock()
        self.definition_file.disconnect = MagicMock()
        self.definition_file.nextChunk = MagicMock()
        self.definition_file.update = MagicMock()
        self.definition_file.saveFile = MagicMock()

        analysis_timestamp = 1234567890
        self.definition_file.updateAnalysisStatus(analysis_timestamp)

        self.definition_file.connect.assert_called_once()
        self.definition_file.disconnect.assert_called_once()
        self.definition_file.nextChunk.assert_called_once()
        self.definition_file.update.assert_called_once_with(
            condition=f"timestamp_created == {analysis_timestamp}",
            attribute='status',
            value='finished'
        )
        self.definition_file.saveFile.assert_called_once()

if __name__ == '__main__':
    unittest.main()
