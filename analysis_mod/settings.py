from dotenv import load_dotenv
import os

class Settings():

    def __init__(self) -> None:
        load_dotenv()
        self.analysis_definition = os.getenv('ANALYSIS_DEFINITION')
        self.__config = {
            'connection_type': self.analysis_definition
        }
        self.__loadConfiguration()

    def __loadConfiguration(self) -> None:
        if self.analysis_definition == 'file':
            self.__config['file_path'] = os.getenv('FILE_PATH')
            self.__config['file_separator'] = os.getenv('FILE_SEPARATOR')
        elif self.analysis_definition == 'database':
            self.__config['database_type'] = os.getenv('DATABASE_TYPE')
            self.__config['database_url'] = os.getenv('DATABASE_URL')
        else:
            raise NotImplementedError('The defined analysis definition is not supported by this program.')

    def getConfiguration(self):
        return self.__config
