#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    url = params.url
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.db_name
    table_name = params.table_name

    gz_file = 'output.csv.gz'
    file_name = 'output.csv'
    os.system(f"wget {url} -O {gz_file}")
    os.system(f"gzip -d {gz_file}")

    rides = pd.read_csv(file_name)

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    engine.connect()

    rides.lpep_pickup_datetime = pd.to_datetime(rides.lpep_pickup_datetime)
    rides.lpep_dropoff_datetime = pd.to_datetime(rides.lpep_dropoff_datetime)

    rides.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    chunksize = 100000

    for i in range(0, len(rides), chunksize):
        chunk = rides.iloc[i: i + chunksize]
        chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f"Inserted rows {i} to {i + len(chunk)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest csv data to postgres db')
    parser.add_argument('--user', help='username of the db')
    parser.add_argument('--password', help='password of the db')
    parser.add_argument('--host', help='host of the db')
    parser.add_argument('--port', help='port of the db')
    parser.add_argument('--db_name', help='name of the database')
    parser.add_argument('--table_name', help='name of the table')
    parser.add_argument('--url', help='url to the .csv.gz file')

    args = parser.parse_args()

    main(args)
