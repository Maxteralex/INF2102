from abc import ABC, abstractclassmethod

class Connection(ABC):

    def __init__(self):
        self.conn = None

    @abstractclassmethod
    def configure(self, conn_settings: dict, chunk_size: int = None) -> None:
        pass

    @abstractclassmethod
    def connect(self) -> None:
        pass

    @abstractclassmethod
    def disconnect(self) -> None:
        pass
