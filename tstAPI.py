import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

langURL = f"https://api.themoviedb.org/3/movie/278/credits?api_key={TMDB_API_KEY}&language=en-US"
langs = requests.get(url=langURL)
langs_data = langs.json()
#results = langs_data.get("results")
print(langs_data['cast'])