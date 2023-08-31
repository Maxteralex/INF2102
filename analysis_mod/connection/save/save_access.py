from abc import ABC, abstractclassmethod


class SaveAccess(ABC):

    @abstractclassmethod
    def saveResults(self, results, query) -> None:
        pass
