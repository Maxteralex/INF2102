import unittest
from unittest.mock import MagicMock
from mapper.analysis_mapper import AnalysisMapper

class TestAnalysisMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of AnalysisMapper
        self.analysis_mapper = AnalysisMapper()
        self.analysis_config = {'analysis_type': 'sentiment'}

    def test_get_analysis(self):
        # Test the getAnalysis method
        mock_analysis_class = MagicMock()
        mock_analysis_instance = MagicMock()
        mock_analysis_class.return_value = mock_analysis_instance
        self.analysis_mapper._getKeyVariable = MagicMock(return_value=mock_analysis_class)

        result = self.analysis_mapper.getAnalysis(self.analysis_config)

        self.assertEqual(result, mock_analysis_instance)
        mock_analysis_class.assert_called_once()
        mock_analysis_instance.assert_called_once_with(self.analysis_config)

if __name__ == '__main__':
    unittest.main()
