import os
import requests
from dotenv import load_dotenv
import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Languages we want to keep
target_langs = ['en', 'ja', 'hi', 'ko', 'it', 'pt', 'es', 'zh', 'fr', 'tr', 'ru']

langURL = f"https://api.themoviedb.org/3/configuration/languages?api_key={TMDB_API_KEY}"
langs = requests.get(url=langURL)
langs_data = langs.json()

# Filter the data to only include our target languages
filtered_langs = [lang for lang in langs_data if lang['iso_639_1'] in target_langs]

#print(filtered_langs)

# If you want to create a DataFrame with the filtered data:
df = pd.DataFrame(filtered_langs)
df.to_csv("langs.csv", index=False)
print(df)