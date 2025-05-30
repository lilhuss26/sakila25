import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

genres_id = [35 ,   18  ,  80   , 12 ,   16  ,  28   , 37  ,  14 ,   27  ,  53 ,10752, 10751 , 10749 ,10402]

genrsURL = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={TMDB_API_KEY}"
genrs = requests.get(url=genrsURL)
genrs_data = genrs.json()

filtered_genrs = [genre for genre in genrs_data['genres'] if genre['id'] in genres_id]

df = pd.DataFrame(filtered_genrs)
df.to_csv("Sakila_csv/category.csv", index=False)
print(df)

