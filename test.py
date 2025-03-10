import os
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
headers = {
    "accept": "application/json"
}
url = f"https://api.themoviedb.org/3/movie/640?api_key={TMDB_API_KEY}"
movie_response = requests.get(url, headers=headers)
print(f"{movie_response.text}\n\n\n\n\n\n")
if movie_response.status_code == 200:
    movie_data = movie_response.json()
    name = movie_data.get("title")
    genres = [{"id": genre["id"], "name": genre["name"]} for genre in movie_data.get("genres", [])]
    
    filtered_response = {
        "name": name,
        "genres": genres
    }
    
    print(filtered_response)
else:
    print(f"Error: {movie_response.status_code}")