import pandas as pd
from neural_model import NeuralModel
from typing import Dict
from transformers import set_seed

class NeuralModelOperations():

    @staticmethod
    def load(labels: Dict[int, str], model_path: str, token_number: int) -> NeuralModel:
        neural_model = NeuralModel(token_number, labels)
        neural_model.load_model(model_path)
        return neural_model
