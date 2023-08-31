from abc import ABC, abstractclassmethod
from pandas import DataFrame


class LoadAccess(ABC):

    @abstractclassmethod
    def initializeQueryConnection(self, query: dict) -> dict:
        pass

    @abstractclassmethod
    def getNextDataChunk(self) -> DataFrame:
        pass
