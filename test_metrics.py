import unittest
from load import LoadData
from update import UpdateData
import pandas as pd
import json


class MyTestCase(unittest.TestCase):
    def test_exists_load(self):
        df = pd.read_parquet('test_5_rows.parquet', engine='pyarrow')

        LoadData.load_json('test_5_rows.parquet')

        with open('json/202211_yellow_taxi_kpis.json') as json_file:
            origin = json.load(json_file)

        with self.subTest():
            self.assertAlmostEqual(origin['avg_price_pre_mile_pre_customer'], 5.975394235997825, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['payment_dist_1'], 0.8, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['payment_dist_2'], 0.2, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['custom_indicator'], 1.4200652528548126, 10)

    def test_exists_update(self):
        df = pd.read_parquet('test_10_rows.parquet', engine='pyarrow')

        UpdateData.update_json('test_10_rows.parquet')

        with open('json/202211_yellow_taxi_kpis.json') as json_file:
            origin = json.load(json_file)

        with self.subTest():
            self.assertAlmostEqual(origin['avg_price_pre_mile_pre_customer'], 3.5681227328281278, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['payment_dist_1'], 0.75, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['payment_dist_2'], 0.25, 10)
        with self.subTest():
            self.assertAlmostEqual(origin['custom_indicator'], 1.0460068132423685, 10)


if __name__ == '__main__':
    unittest.main()
