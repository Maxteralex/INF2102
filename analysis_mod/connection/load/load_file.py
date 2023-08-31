from pandas import DataFrame

from connection.load import LoadAccess
from connection import FileConnection


class LoadFile(LoadAccess, FileConnection):

    def initializeQueryConnection(self, query: dict) -> None:
        self.connect()
        self.query_dict = query

    def getNextDataChunk(self) -> DataFrame:
        self.nextChunk()
        if self.getChunk() is None:
            return None
        return self._filterData()

    def _filterData(self):
        if self.query_dict.get('columns') is not None:
            self.selectColumns(self.query_dict['columns'])
        if self.query_dict.get('filters') is not None:
            return self.query(self.query_dict['filters'])
        else:
            return self.getChunk()
