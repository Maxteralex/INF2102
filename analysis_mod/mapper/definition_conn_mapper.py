from mapper.mapper import Mapper
from connection import definition as de

class DefinitionAccessMapper(Mapper):

    def __init__(self):
        self.mapper_dict = {
            'database': de.DefinitionDatabase,
            'file': de.DefinitionFile
        }

    def getConnection(self, definition_conn_config: dict) -> de.DefinitionAccess:
        definition_conn_class = self._getKeyVariable(definition_conn_config['connection_type'])
        definition_conn = definition_conn_class()
        definition_conn.configure(definition_conn_config)
        return definition_conn