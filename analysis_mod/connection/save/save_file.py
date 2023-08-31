from pandas import DataFrame

from connection.save import SaveAccess
from connection import FileConnection


class SaveFile(SaveAccess, FileConnection):

    def saveResults(self, results, query:dict) -> None:
        self._setConnection(results)
        self.saveFile(partial=True)
        self.disconnect()

    def _setConnection(self, connection: DataFrame):
        self.conn = connection
        self.chunk = self.conn
        self.chunk_index += 1