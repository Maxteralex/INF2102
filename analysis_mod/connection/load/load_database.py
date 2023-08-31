from pandas import DataFrame

from connection.load import LoadAccess
from connection import DatabaseConnection


class LoadDatabase(LoadAccess, DatabaseConnection):

    def initializeQueryConnection(self, query: dict) -> dict:
        self.connect()
        pass

    def getNextDataChunk(self) -> DataFrame:
        
        pass
