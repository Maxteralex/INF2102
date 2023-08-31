from transformers import BertForSequenceClassification, AutoTokenizer
from torch.utils.data import DataLoader, Dataset
from typing import List, Dict, Tuple
from torch import nn
import pandas as pd
import numpy as np
import torch


class TextClassDataset(Dataset):
    def __init__(self, x:np.array, y:np.array):
        self.data = [(x[i], y[i]) for i in range(len(x))]

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index:int) -> tuple:
        return self.data[index]

class NeuralModel():
    def __init__(self, max_seq_length: int, labels: Dict[int, str]):
        # The neural model to be used
        self.__model = BertForSequenceClassification.from_pretrained('neuralmind/bert-large-portuguese-cased', num_labels=len(labels))

        # The model tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained('neuralmind/bert-large-portuguese-cased', do_lower_case=True)

        # The device to run the model
        self.device = "cpu"

        # The tokenizer parameters
        self.param_tk = {
            'return_tensors': "pt",
            'padding': 'max_length',
            'max_length': max_seq_length,
            'add_special_tokens': True,
            'truncation': True
        }

        # The class labels
        self.__index_labels = labels


    def load_model(self, input_dir: str="./"):
        model_state_dict = torch.load(input_dir + 'bert_model.bin', map_location=torch.device(self.device))
        self.__model = BertForSequenceClassification.from_pretrained(input_dir + 'bert_config.bin', num_labels=len(self.__index_labels), state_dict=model_state_dict)


    def classify(self, dataset:pd.DataFrame, batch_size:int) -> Tuple[List[int], List[float]]:
        x_sampled = np.array(dataset['item'].fillna(''), dtype=object)
        y_sampled = np.zeros(len(x_sampled))
        dataloader_set = TextClassDataset(x_sampled, y_sampled)
        valid_loader = DataLoader(dataloader_set, batch_size=batch_size, shuffle=False)

        y_valid_pred = []
        y_valid_prob = []

        with torch.no_grad():
            for batch in valid_loader:
                # Input features and labels from batch and move to device
                x_valid_bt, y_valid_bt = batch

                x_valid_bt = list(x_valid_bt)
                y_valid_bt = list(y_valid_bt)

                x_valid_bt = self.tokenizer(x_valid_bt, **self.param_tk).to(self.device)

                logits = self.__model(**x_valid_bt, return_dict=False)[0]
                softmax_logits = nn.functional.softmax(logits, dim=1).cpu().detach().numpy()

                y_valid_pred.extend(np.argmax(softmax_logits, axis=1))
                y_valid_prob.extend(np.max(softmax_logits, axis=1))

        return y_valid_pred, y_valid_prob
