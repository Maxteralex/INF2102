import json
from pandas import DataFrame
import requests

from analysis import DataAnalysis


class SentimentAnalysis(DataAnalysis):

    def process(self):
        # Initializes the query connection
        self.load_connection.initializeQueryConnection(
            query=self.load_queries.sentimentAnalysisQuery()
        )

        # Gets the next data chunk
        data_chunk = self.load_connection.getNextDataChunk()

        while data_chunk is not None:
            # Analyzes the data chunk
            results = self.classify(data_chunk)
        
            self.save_connection.saveResults(
                results=results,
                query=self.save_queries.sentimentAnalysisInsert()
            )

            # Gets the next data chunk
            data_chunk = self.load_connection.getNextDataChunk()

    def classify(self, data_chunk: DataFrame):

        send_data = data_chunk['text'].tolist()

        request_data = json.dumps([{'item': text} for text in send_data])

        headers = {'Content-Type': 'application/json'}

        # Runs the request and gets the response
        response = requests.post('http://localhost:5000/classify', data=request_data, headers=headers)
        response_data = response.json()

        # Obtain the classification from the response
        result_df = data_chunk.copy(deep = True)
        result_df['classification'] = response_data['classification']

        return result_df[['id', 'classification']]