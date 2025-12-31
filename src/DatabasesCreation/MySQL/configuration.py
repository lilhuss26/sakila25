import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from src.FetchData.FetchData import FetchData

fetcher = FetchData()

load_dotenv()
connection_string = os.getenv('MYSQL_STRING')

temp_engine = create_engine(connection_string)
with temp_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS sakila25"))
    conn.commit()

sakila25_engine = create_engine(connection_string + "/sakila25")