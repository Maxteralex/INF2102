import pandas as pd
from typing import List, Any

from connection.connection import Connection


class FileConnection(Connection):

    connection_method = {
        'csv': pd.read_csv, 'xlsx': pd.read_excel, 'xls': pd.read_excel,
        'json': pd.read_json, 'html': pd.read_html, 'xml': pd.read_xml
    }

    def configure(self, conn_settings: dict, chunk_size: int = None):
        self.path = conn_settings.get('file_path')
        self.extension = self.path.split('.')[-1]
        self.separator = conn_settings.get('file_separator')
        self.chunk_size = chunk_size
        self.chunk = None
        self.chunk_index = -1

    def connect(self) -> None:
        if self.conn is not None:
            self.disconnect()
        method = self.connection_method.get(self.extension)
        if method is not None:
            if self.extension == 'csv' and self.separator is not None:
                self.conn = method(self.path, sep=self.separator, chunksize=self.chunk_size)
            else:
                self.conn = method(self.path, chunksize=self.chunk_size)
        else:
            raise NotImplementedError('The given file extension is not supported.')

    def disconnect(self) -> None:
        if self.conn is not None:
            self.conn = None
            self.chunk = None

    def nextChunk(self):
        if self.chunk_size is None:
            self.chunk = self.conn
        else:
            try:
                self.chunk = next(self.conn)
            except:
                self.disconnect()

    def getChunk(self):
        return self.chunk

    def query(self, filters: List[str], skiprows: int = 0, nrows: int = 10000, order_by: List[str] = None) -> pd.DataFrame:
        if self.chunk is not None:
            result = None

            if len(filters) > 0:
                result = self.chunk.query(
                    ' and '.join(filters)
                )[skiprows:nrows]
            else:
                result = self.chunk[skiprows:nrows]
            
            if order_by is not None:
                return result.sort_values(by=order_by)
            return result

    def selectColumns(self, columns: List[str]):
        self.chunk = self.chunk[columns]

    def update(self, condition: str, attribute: str, value: Any):
        if self.conn is not None:
            rows_to_update = self.chunk.query(condition).index
            self.chunk.loc[rows_to_update, attribute] = value

    def saveFile(self, partial: bool=False):
        df = self.chunk
        save_methods = {
            'csv': df.to_csv, 'xlsx': df.to_excel, 'xls': df.to_excel,
            'json': df.to_json, 'html': df.to_html, 'xml': df.to_xml
        }
        save_method = save_methods.get(self.extension)

        if partial is False:
            path = self.path
        else:
            path = self._partialPath()

        if self.extension in ['xlsx', 'xls']:
            with pd.ExcelWriter(path, engine='xlsxwriter') as excel_writer:
                save_method(excel_writer)
        else:
            save_method(path)

    def _partialPath(self):
        """
        Changes the path to 
        """
        extension_index = self.path.rfind('.')
        return f'{self.path[:extension_index]}{self.chunk_index}{self.path[extension_index:]}'