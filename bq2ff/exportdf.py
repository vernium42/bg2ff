import numpy as np
import pandas as pd
from pandas.core.dtypes.dtypes import DatetimeTZDtype
import pyarrow as pa
import pyarrow.parquet as pq


class TypeBase:
    def __init__(self):
        self.writer = None

    def __del__(self):
        if self.writer:
            self.writer.close()

    def create(self, df, path):
        raise Exception("`create` function not implemented")

    def append(self, df):
        raise Exception("`append` function not implemented")


class TypeCSV(TypeBase):
    def __init__(self):
        super().__init__()

    def create(self, df, path):
        self.writer = open(path, 'w+', newline='')
        df.to_csv(self.writer, index=False)

    def append(self, df):
        df.to_csv(self.writer, mode='a', header=False, index=False)


class TypeExcel(TypeBase):
    def __init__(self):
        super().__init__()
        self.last_row = 0

    def autosize_excel_columns_df(self, sheetname, df, offset=0):
        worksheet = self.writer.sheets[sheetname]
        for idx, col in enumerate(df):
            series = df[col]
            max_len = max((
              series.astype(str).map(len).max(),
              len(str(series.name))
            )) + 1
            worksheet.set_column(idx+offset, idx+offset, max_len)

    @staticmethod
    def make_dt_naive(df):
        cols = df.select_dtypes(include=[DatetimeTZDtype, np.datetime64]).columns
        for col in cols:
            df[col] = df[col].dt.tz_localize(None)

    def create(self, df, path):
        self.writer = pd.ExcelWriter(path)
        self.make_dt_naive(df)
        df.to_excel(self.writer, index=False)
        self.autosize_excel_columns_df('Sheet1', df)
        self.last_row += len(df)

    def append(self, df):
        self.make_dt_naive(df)
        df.to_excel(self.writer, startrow=self.last_row, index=False, header=False)
        self.last_row += len(df)


class TypeParquet(TypeBase):
    def __init__(self):
        super().__init__()

    def create(self, df, path):
        table = pa.Table.from_pandas(df)
        self.writer = pq.ParquetWriter(path, table.schema)
        self.writer.write_table(table)

    def append(self, df):
        table = pa.Table.from_pandas(df)
        self.writer.write_table(table)


class ExportDF:
    def __init__(self, export_path, file_type):
        self.export_path = export_path
        self.type_handler = self.type_factory(file_type)
        self.is_created = False

    @staticmethod
    def type_factory(file_type):
        if file_type == 'csv':
            return TypeCSV()
        elif file_type == 'excel':
            return TypeExcel()
        elif file_type == 'parquet':
            return TypeParquet()

        raise Exception("File format not supported.")

    def save(self, df):
        if self.is_created:
            self.type_handler.append(df)
        else:
            self.type_handler.create(df, self.export_path)
            self.is_created = True
