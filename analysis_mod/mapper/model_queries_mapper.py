from mapper.mapper import Mapper
import model_queries as mq

class ModelQueriesMapper(Mapper):

    def __init__(self):
        self.mapper_dict = {
            'database': mq.RelationalDatabaseQueries,
            'file': mq.FileQueries
        }

    def getQueries(self, conn_type: str, analysis_timestamp: int) -> mq.ModelQueries:
        model_queries_class = self._getKeyVariable(conn_type)
        return model_queries_class(analysis_timestamp)
