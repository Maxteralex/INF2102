from typing import Any

class Mapper():

    def __init__(self) -> None:
        self.mapper_dict = dict()

    def _getKeyVariable(self, key: Any) -> Any:
        variable_class = self.mapper_dict.get(key)
        if variable_class is not None:
            return variable_class
        raise ModuleNotFoundError('This key parameter was not mapped.')