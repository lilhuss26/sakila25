import requests
from typing import List
def top_rated_movies_ids(key: str, pages: int = 6) -> List[int]:
    movie_ids = []
    for i in range(1, pages):
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={key}&page={i}&language=en-US"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = data.get("results", [])
            movie_ids.extend([movie["id"] for movie in results])
        except requests.RequestException as e:
            print(f"Error fetching page {i}: {e}")
    return movie_ids
