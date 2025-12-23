import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from src.FetchData.FetchData import FetchData

fetcher = FetchData()

load_dotenv()
connection_string = os.getenv('MYSQL_STRING')

sakila25_engine = create_engine(connection_string + "/sakila25")