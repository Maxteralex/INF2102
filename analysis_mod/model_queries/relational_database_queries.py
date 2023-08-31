from model_queries import ModelQueries


class RelationalDatabaseQueries(ModelQueries):

    def sentimentAnalysisQuery(self) -> dict:
        return self._postsTextClassificationQuery()

    def toxicAnalysisQuery(self) -> dict:
        return self._postsTextClassificationQuery()

    def _postsTextClassificationQuery(self) -> dict:
        return {'query': f'SELECT id, text FROM post WHERE analysis = {self.analysis_timestamp}'}