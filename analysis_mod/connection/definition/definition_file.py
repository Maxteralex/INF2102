from connection.definition import DefinitionAccess
from connection import FileConnection


class DefinitionFile(DefinitionAccess, FileConnection):

    def getNextScheduledAnalysisConfiguration(self) -> dict:
        self.connect()
        self.nextChunk()
        next_analysis = self.query(
            filters=["status == 'waiting'"],
            nrows=1,
            order_by=['timestamp_created']).to_dict(orient='index').get(0)
        self.disconnect()
        return next_analysis

    def updateAnalysisStatus(self, analysis_timestamp: int) -> None:
        self.connect()
        self.nextChunk()
        self.update(
            condition=f"timestamp_created == {analysis_timestamp}",
            attribute='status',
            value='finished'
        )
        self.saveFile()
        self.disconnect()
