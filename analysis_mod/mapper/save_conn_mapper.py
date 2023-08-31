from mapper.mapper import Mapper
import connection.save as cs

class SaveConnectionMapper(Mapper):

    def __init__(self):
        self.mapper_dict = {
            'database': cs.SaveDatabase,
            'file': cs.SaveFile
        }

    def getConnection(self, save_config: dict) -> cs.SaveAccess:
        save_conn_class = self._getKeyVariable(save_config['connection_type'])
        save_conn = save_conn_class()
        save_conn.configure(save_config)
        return save_conn
