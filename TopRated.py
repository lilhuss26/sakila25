import os
import requests
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

topurl = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&page=1"
topRated = requests.get(url=topurl)
print(topRated.text)