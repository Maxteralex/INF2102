from settings import Settings
from definition.analysis_definition import AnalysisDefinition

if __name__ == '__main__':
    # Load settings
    definition_config = Settings().getConfiguration()

    # Define the analysis
    definition = AnalysisDefinition(definition_config)
    analysis = definition.getNextAnalysis()

    # Run analysis
    analysis.process()

    # Update the analysis status after the process is finished
    definition.updateAnalysis(analysis.getTimestampCreated())
