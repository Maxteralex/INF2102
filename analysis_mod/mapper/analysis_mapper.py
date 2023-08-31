from mapper.mapper import Mapper
import analysis as an


class AnalysisMapper(Mapper):

    def __init__(self):
        self.mapper_dict = {
            'sentiment': an.SentimentAnalysis,
            # 'toxic': an.ToxicAnalysis
        }

    def getAnalysis(self, analysis_config: dict) -> an.DataAnalysis:
        analysis_class = self._getKeyVariable(analysis_config['analysis_type'])
        return analysis_class(analysis_config)