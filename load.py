import sys
import json
import pandas as pd


# This script loads a new parquet file.
# For this it separates them by dates to save them independently in json files.
# For each json file it will generate the required metrics.
class LoadData:
    def load_json(path):
        df = pd.read_parquet(path, engine='pyarrow')
        df["tpep_pickup_date"] = pd.to_datetime(df['tpep_pickup_datetime']).dt.date
        for day in df["tpep_pickup_date"].unique():
            dic = {}
            df_day = df.loc[df['tpep_pickup_date'] == day]
            year = str(day.year)
            month = str(day.month)
            day = str(day.day)
            samples = len(df_day.index)

            dic["avg_price_pre_mile_pre_customer"] = (df_day["total_amount"].mean() / df_day[
                "passenger_count"].mean()) / df_day["trip_distance"].mean()

            values = df_day["payment_type"].value_counts()
            for index, val in values.items():
                dic["payment_dist_" + str(index)] = val / samples

            dic["custom_indicator"] = (df_day["tip_amount"].mean() + df_day["extra"].mean()) / df_day[
                "trip_distance"].mean()

            dic["samples"] = samples

            print("Create " + "json/" + year + month + day + "_yellow_taxi_kpis.json")
            with open("json/" + year + month + day + "_yellow_taxi_kpis.json", "w") as outfile:
                json.dump(dic, outfile)


if __name__ == "__main__":
    LoadData.load_json(sys.argv[1])
