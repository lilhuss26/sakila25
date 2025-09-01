import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

base_link = f"https://api.themoviedb.org/3/watch/providers/movie?api_key={TMDB_API_KEY}&language=en-US&watch_region=US"
providers = requests.get(url=base_link)
providers_data = providers.json()
print(providers_data)