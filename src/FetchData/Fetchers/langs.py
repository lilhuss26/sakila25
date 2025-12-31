import requests

def langs(key: str):
    target_langs = ['en', 'ja', 'hi', 'ko', 'it', 'pt', 'es', 'zh', 'fr', 'tr', 'ru']

    lang_url = f"https://api.themoviedb.org/3/configuration/languages?api_key={key}"
    langs = requests.get(url=lang_url)
    langs_data = langs.json()
    print("langs_data fetched successfully")
    return {
        lang['iso_639_1']: {
            'language_iso_639_1': lang['iso_639_1'],
            'english_name': lang['english_name'],
            'name': lang['name']
        }
        for lang in langs_data
        if lang['iso_639_1'] in target_langs
    }
