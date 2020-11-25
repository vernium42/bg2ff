from .exportdf import ExportDF

class BQ2FF:
    def __init__(self, bq_client, iter_row_size=10000):
        self.client = bq_client
        self.iter_row_size = iter_row_size

    def export(self, query, export_path, file_type, lower_case=False):
        dfs = self.client.query(query).result(self.iter_row_size) \
            .to_dataframe_iterable()
        export_t = ExportDF(export_path, file_type)
        for df in dfs:
            if lower_case:
                df.columns = [col.lower() for col in df.columns]
            export_t.save(df)
