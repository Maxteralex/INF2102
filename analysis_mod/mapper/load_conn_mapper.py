from mapper.mapper import Mapper
import connection.load as cl

class LoadConnectionMapper(Mapper):

    def __init__(self):
        self.mapper_dict = {
            'database': cl.LoadDatabase,
            'file': cl.LoadFile
        }

    def getConnection(self, load_config: dict, chunk_size: int) -> cl.LoadAccess:
        load_conn_class = self._getKeyVariable(load_config['connection_type'])
        load_conn = load_conn_class()
        load_conn.configure(load_config, chunk_size)
        return load_conn