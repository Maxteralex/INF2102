from abc import ABC, abstractclassmethod


class ModelQueries(ABC):

    def __init__(self, analysis_timestamp):
        self.analysis_timestamp = analysis_timestamp

    @abstractclassmethod
    def sentimentAnalysisQuery(self) -> dict:
        pass

    @abstractclassmethod
    def toxicAnalysisQuery(self) -> dict:
        pass

    @abstractclassmethod
    def sentimentAnalysisInsert(self) -> dict:
        pass