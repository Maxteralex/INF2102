from abc import ABC, abstractclassmethod


class DefinitionAccess(ABC):

    @abstractclassmethod
    def getNextScheduledAnalysisConfiguration(self) -> dict:
        pass

    @abstractclassmethod
    def updateAnalysisStatus(self, analysis_timestamp: int) -> None:
        pass
