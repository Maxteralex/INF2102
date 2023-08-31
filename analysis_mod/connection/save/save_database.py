from connection.save import SaveAccess
from connection import DatabaseConnection


class SaveDatabase(SaveAccess, DatabaseConnection):

    def getNextScheduledAnalysisConfiguration(self) -> dict:
        self.connect()
        next_analysis = self.query(
            filters="status == 'waiting'",
            nrows=1,
            order_by=['timestamp_created']).to_dict().get(0)
        self.disconnect()
        return next_analysis

    def updateAnalysisStatus(self, analysis_timestamp: int) -> None:
        self.connect()
        self.update(
            condition=f"timestamp_created == {analysis_timestamp}",
            attribute='status',
            value='finished'
        )
        self.disconnect()
