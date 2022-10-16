import time
import json
from os.path import exists
import pandas as pd


def update_json(path):
    df = pd.read_parquet(path, engine='pyarrow')
    df["tpep_pickup_date"] = pd.to_datetime(df['tpep_pickup_datetime']).dt.date
    for day in df["tpep_pickup_date"].unique():
        dic = {}
        df_day = df.loc[df['tpep_pickup_date'] == day]
        year = str(day.year)
        month = str(day.month)
        day = str(day.day)
        samples = len(df_day.index)
        json_file_name = "json/" + year + month + day + "_yellow_taxi_kpis.json"
        if exists(json_file_name):
            with open(json_file_name) as json_file:
                origin = json.load(json_file)

            per_origin = origin['samples'] / (origin['samples'] + samples)
            per_act = samples / (origin['samples'] + samples)

            dic["avg_price_pre_mile_pre_customer"] = (((df_day["total_amount"].mean() / df_day["passenger_count"].mean()) / df_day["trip_distance"].mean()) * per_act) + (origin['avg_price_pre_mile_pre_customer'] * per_origin)

            values = df_day["payment_type"].value_counts()
            for index, val in values.items():
                dic["payment_dist_" + str(index)] = ((val / samples) * per_act) + (origin["payment_dist_" + str(index)] * per_origin)

            dic["custom_indicator"] = (((df_day["tip_amount"].mean() + df_day["extra"].mean()) / df_day["trip_distance"].mean()) * per_act) + (origin['custom_indicator'] * per_origin)

            dic["samples"] = origin['samples'] + samples

            print("Update "+json_file_name)
            with open(json_file_name, "w") as outfile:
                json.dump(dic, outfile)
        else:
            dic["avg_price_pre_mile_pre_customer"] = (df_day["total_amount"].mean() / df_day[
                "passenger_count"].mean()) / \
                                                     df_day["trip_distance"].mean()

            values = df_day["payment_type"].value_counts()
            for index, val in values.items():
                dic["payment_dist_" + str(index)] = val / samples

            dic["custom_indicator"] = (df_day["tip_amount"].mean() + df_day["extra"].mean()) / df_day[
                "trip_distance"].mean()

            dic["samples"] = samples

            print("Create "+json_file_name)
            with open(json_file_name, "w") as outfile:
                json.dump(dic, outfile)


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

        dic["avg_price_pre_mile_pre_customer"] = (df_day["total_amount"].mean() / df_day["passenger_count"].mean()) / \
                                                 df_day["trip_distance"].mean()

        values = df_day["payment_type"].value_counts()
        for index, val in values.items():
            dic["payment_dist_" + str(index)] = val / samples

        dic["custom_indicator"] = (df_day["tip_amount"].mean() + df_day["extra"].mean()) / df_day[
            "trip_distance"].mean()

        dic["samples"] = samples

        print("Create "+"json/" + year + month + day + "_yellow_taxi_kpis.json")
        with open("json/" + year + month + day + "_yellow_taxi_kpis.json", "w") as outfile:
            json.dump(dic, outfile)


def main():
    start = time.time()

    # update_json('yellow_tripdata_2022-01.parquet')

    df = pd.read_parquet('yellow_tripdata_2022-01.parquet', engine='pyarrow')
    df.head(5).to_csv('test_5_rows.csv')
    df = pd.read_csv('test_5_rows.csv')
    print(df)

    end = time.time()
    print("Total time: " + str(end - start))


main()
