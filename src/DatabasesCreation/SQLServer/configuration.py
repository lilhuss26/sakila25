import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from src.FetchData.FetchData import FetchData

fetcher = FetchData()

load_dotenv()
connection_string = os.getenv('SQLSERVER_STRING')

sakila25_engine = create_engine(connection_string)