import requests

def categories(key: str):
    genres_id = [35, 18, 80, 12, 16, 28, 37, 14, 27, 53, 10752, 10751, 10749, 10402]

    genrsURL = f"https://api.themoviedb.org/3/genre/movie/list?language=en&api_key={key}"
    genrs = requests.get(url=genrsURL)
    genrs_data = genrs.json()
    return {genre['id']: {'category_id': genre['id'], 'name': genre['name']} for genre in genrs_data['genres'] if
            genre['id'] in genres_id}