import os
from src.FetchData.FetchData import FetchData

DIR = "Sakila25_csv"
fetcher = FetchData()

# Create directory if it doesn't exist
os.makedirs(DIR, exist_ok=True)