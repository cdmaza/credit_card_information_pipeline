import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, Table, Column, String, MetaData


CSV_DIRECTORY = './data'
DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@localhost:5432/weather_forecast_db'

"""
function iterate all csv files and upload using upload_csv_to_postgres
using sqlalchemy
"""

def upload_to_postgres(csv_file):
    engine = create_engine(DATABASE_URI)
    
    file_path = os.path.join(CSV_DIRECTORY, csv_file)
    df = pd.read_csv(file_path)
    
    table_name = os.path.splitext(csv_file)[0]
    
    with engine.connect() as connection:
        df.to_sql(
            table_name,
            connection,
            if_exists='replace',  # Options: 'fail', 'replace', 'append'
            index=False
        )


def upload():
    csv_files = [f for f in os.listdir(CSV_DIRECTORY) if f.endswith('.csv')]
    for csv_file in csv_files:
        upload_to_postgres(csv_file)