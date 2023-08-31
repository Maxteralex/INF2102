from analysis import DataAnalysis
from mapper.definition_conn_mapper import DefinitionAccessMapper
from mapper.analysis_mapper import AnalysisMapper

class AnalysisDefinition():

    def __init__(self, definition_config):
        self.definition_access = DefinitionAccessMapper().getConnection(definition_config)

    def getNextAnalysis(self) -> DataAnalysis:
        # Gets the analysis configuration
        analysis_config = self.definition_access.getNextScheduledAnalysisConfiguration()

        # Initializes the analysis given the configuration
        return AnalysisMapper().getAnalysis(analysis_config)

    def updateAnalysis(self, analysis_timestamp: int):
        # Updates the analysis in the definition data access object
        self.definition_access.updateAnalysisStatus(analysis_timestamp)
