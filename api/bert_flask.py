from flask import Flask, jsonify, request
import pandas as pd
from ml_operations import NeuralModelOperations
from preprocess import Preprocess

app = Flask(__name__)

labels = {0: 'negative', 1: 'neutral', 2: 'positive'}
neural_model = NeuralModelOperations.load(
    labels=labels,
    model_path='model\\',
    token_number=64
)

@app.route('/classify', methods=['POST'])
def classify():
    documents = request.get_json()

    document_df = pd.DataFrame(documents)

    preprocessed_df = Preprocess().preprocessData(document_df)

    classification = neural_model.classify(preprocessed_df, batch_size=8)

    classes_labels = [
        labels.get(prediction)
        for prediction in classification[0]
    ]

    # Retorne a resposta em formato JSON
    return jsonify({'classification': classes_labels, 'probability': float(classification[1][0])})

if __name__ == '__main__':
    app.run()