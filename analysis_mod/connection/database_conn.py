from abc import abstractclassmethod
from pandas import DataFrame

from connection.connection import Connection


class DatabaseConnection(Connection):

    def configure(self, conn_settings: dict, chunk_size: int = None) -> None:
        self.database_name = conn_settings['database_name']
        self.url = conn_settings['url']
        self.chunk_size = chunk_size
        self.engine = self._prepareSpecificDatabaseEngine()

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    @abstractclassmethod
    def _prepareSpecificDatabaseEngine(self):
        pass

    @abstractclassmethod
    def query(self) -> DataFrame:
        pass