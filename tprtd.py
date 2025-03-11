import os
import requests
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
headers = {
    "accept": "application/json",
    "Authorization": TMDB_TOKEN
}

topurl = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US"
topRated = requests.get(url=topurl,headers=headers)
print(topRated.text)