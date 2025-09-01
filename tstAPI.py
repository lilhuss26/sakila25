import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

tst_url = f"https://api.themoviedb.org/3/movie/287/watch/providers?api_key={TMDB_API_KEY}&language=en-US"
tst = requests.get(url=tst_url)
tst_data = tst.json()
print(tst_data)