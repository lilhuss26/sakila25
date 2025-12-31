from src.DatabasesCreation.MySQL.configuration import sakila25_engine
from sqlalchemy.orm import Session
session = Session(sakila25_engine)
from src.DatabasesCreation.MySQL.Schema import Language,Film,Category,FilmCategory,Actor,FilmActor

def mysql_insert_langs(language_data):
    for iso_code, lang_info in language_data.items():
        lang_info['language_iso_639_1'] = iso_code
        session.merge(Language(**lang_info))
    session.commit()
    print("Languages inserted successfully")

def mysql_insert_film(film_data):
    for film_id, film_info in film_data.items():
        film_info['film_id'] = film_id
        session.merge(Film(**film_info))
    session.commit()
    print("Films inserted successfully")

def mysql_insert_category(category_data):
    for category_id, category_info in category_data.items():
        category_info['category_id'] = category_id
        session.merge(Category(**category_info))
    session.commit()
    print("Categories inserted successfully")

def mysql_insert_actor(actor_data):
    for actor_id, actor_info in actor_data.items():
        actor_info['actor_id'] = actor_id
        session.merge(Actor(**actor_info))
    session.commit()
    print("Actors inserted successfully")

def mysql_insert_film_actor(film_actor_data):
    for film_actor in film_actor_data:
        session.merge(FilmActor(**film_actor))
    session.commit()
    print("Film actors inserted successfully")

def mysql_insert_film_category(film_category_data):
    for film_id, film_category_info in film_category_data.items():
        session.merge(FilmCategory(film_id=film_id,
                                   category_id=film_category_info["category_id"]))

    session.commit()
    print("Film categories inserted successfully")
