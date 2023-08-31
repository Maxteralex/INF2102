from model_queries import ModelQueries


class FileQueries(ModelQueries):

    def sentimentAnalysisQuery(self) -> dict:
        return self._postsTextClassificationQuery()

    def toxicAnalysisQuery(self) -> dict:
        return self._postsTextClassificationQuery()

    def _postsTextClassificationQuery(self) -> dict:
        return {'filters': [], 'columns': ['id', 'text']}

    def sentimentAnalysisInsert(self) -> dict:
        return None

    def toxicAnalysisInsert(self) -> dict:
        return None