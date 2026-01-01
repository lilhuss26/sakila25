import os
from dotenv import load_dotenv
from pymongo import MongoClient
from src.FetchData.FetchData import FetchData

fetcher = FetchData()

load_dotenv()
connection_string = os.getenv('MONGODB_STRING')

client = MongoClient(connection_string)
sakila25_db = client['sakila25']
