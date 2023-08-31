import requests
import json
from pandas import DataFrame


class Classifier:

    @staticmethod
    def classify(df: DataFrame):

        send_data = df['text'].tolist()
        request_data = json.dumps([{'item': text} for text in send_data])
        headers = {'Content-Type': 'application/json'}

        # Runs the request and gets the response
        response = requests.post('http://localhost:5000/classify', data=request_data, headers=headers)
        response_data = response.json()

        # Obtain the classification from the response
        # classification = response_data['classification'][0]
        classification = {"class": response_data['classification'][0], "probability": response_data['probability']}
        return classification

if __name__ == '__main__':
    df = DataFrame([{
        'text': 'vai para a merda'
    }])
    result = Classifier.classify(df)
    print(result)