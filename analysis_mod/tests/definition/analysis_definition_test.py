import unittest
from unittest.mock import MagicMock
from definition.analysis_definition import AnalysisDefinition
import analysis as an

class TestAnalysisDefinition(unittest.TestCase):

    def setUp(self):
        # Create an instance of AnalysisDefinition
        self.analysis_definition = AnalysisDefinition({})
        self.analysis_config = {'analysis_type': 'sentiment'}
        self.analysis_instance = an.SentimentAnalysis({})
        self.definition_access_mock = MagicMock()
        self.definition_access_mock.getNextScheduledAnalysisConfiguration.return_value = self.analysis_config
        self.definition_access_mock.updateAnalysisStatus.return_value = None
        self.analysis_mapper_mock = MagicMock()
        self.analysis_mapper_mock.getAnalysis.return_value = self.analysis_instance
        self.analysis_definition.definition_access = self.definition_access_mock
        self.analysis_definition.analysis_mapper = self.analysis_mapper_mock

    def test_get_next_analysis(self):
        # Test the getNextAnalysis method
        result = self.analysis_definition.getNextAnalysis()
        self.assertEqual(result, self.analysis_instance)
        self.definition_access_mock.getNextScheduledAnalysisConfiguration.assert_called_once()
        self.analysis_mapper_mock.getAnalysis.assert_called_once_with(self.analysis_config)

    def test_update_analysis(self):
        # Test the updateAnalysis method
        analysis_timestamp = 1234567890
        self.analysis_definition.updateAnalysis(analysis_timestamp)
        self.definition_access_mock.updateAnalysisStatus.assert_called_once_with(analysis_timestamp)

if __name__ == '__main__':
    unittest.main()
