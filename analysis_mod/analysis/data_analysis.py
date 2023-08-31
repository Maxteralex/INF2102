from abc import ABC, abstractclassmethod

from mapper.load_conn_mapper import LoadConnectionMapper
from mapper.save_conn_mapper import SaveConnectionMapper
from mapper.model_queries_mapper import ModelQueriesMapper


class DataAnalysis(ABC):

    def __init__(self, analysis_config: dict):
        self.timestamp_created = analysis_config['timestamp_created']
        self.status = analysis_config['status']
        self.load_connection = LoadConnectionMapper().getConnection(
            analysis_config['load_config'], chunk_size=10
        )
        self.load_queries = ModelQueriesMapper().getQueries(
            analysis_config['load_config']['connection_type'], self.timestamp_created
        )
        self.save_connection = SaveConnectionMapper().getConnection(
            analysis_config['save_config']
        )
        self.save_queries = ModelQueriesMapper().getQueries(
            analysis_config['save_config']['connection_type'], self.timestamp_created
        )

    @abstractclassmethod
    def process(self):
        pass

    def getTimestampCreated(self):
        return self.timestamp_created