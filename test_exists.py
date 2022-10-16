import unittest
from load import LoadData
from update import UpdateData
import pandas as pd
import pathlib as pl


class MyTestCase(unittest.TestCase):
    def test_exists_load(self):
        df = pd.read_parquet('test_5_rows.parquet', engine='pyarrow')

        LoadData.load_json('test_5_rows.parquet')

        path = pl.Path('json/202211_yellow_taxi_kpis.json')
        self.assertEquals((str(path), path.is_file()), (str(path), True))



    def test_exists_update(self):
        df = pd.read_parquet('test_10_rows.parquet', engine='pyarrow')

        UpdateData.update_json('test_10_rows.parquet')

        path = pl.Path('json/202211_yellow_taxi_kpis.json')
        self.assertEquals((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()
