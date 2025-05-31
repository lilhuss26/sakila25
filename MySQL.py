import os
from GetAPI import *
from sqlalchemy import create_engine, Index
from dotenv import load_dotenv
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import (SmallInteger,Boolean, DateTime,TEXT,
                        Column, DECIMAL,VARCHAR, Integer, String, ForeignKey, BigInteger)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql import text

# MYSQL_STRING=mysql+pymysql://username:password@localhost:3306

load_dotenv()
connection_string = os.getenv('MYSQL_STRING')

root_engine = create_engine(connection_string)
with root_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS sakila25"))
    conn.commit()

sakila25_engine = create_engine(connection_string + "/sakila25")
Base = declarative_base()

class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer,primary_key=True)
    title = Column(VARCHAR(255))
    rating = Column(DECIMAL(4,3))
    description = Column(TEXT)
    release_date = Column(DateTime)
    language_iso_639_1 = Column(VARCHAR(3), ForeignKey('language.language_iso_639_1'))
    popularity = Column(DECIMAL(6,4))
    revenue = Column(BigInteger)
    runtime = Column(SmallInteger)
    adult = Column(Boolean)

    __table_args__ = (
        Index('idx_title', 'title'), 
        Index('idx_fk_language_id', 'language_iso_639_1'),  
    )

    
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(25))


class FilmCategory(Base):
    __tablename__ = 'film_category'
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'), primary_key=True)

    __table_args__ = (
        Index('idx_fk_film_id', 'film_id'),  
        Index('idx_fk_category_id', 'category_id'),  
    )


class Language(Base):
    __tablename__ = 'language'
    language_iso_639_1 = Column(VARCHAR(3),primary_key=True)
    english_name = Column(VARCHAR(10))
    name = Column(VARCHAR(10))

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer,primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))

    __table_args__ = (
        Index('idx_actor_last_name', 'last_name'),  
    )

class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer,ForeignKey('actor.actor_id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    character = Column(TEXT)
    __table_args__ = (
        Index('idx_fk_film_id', 'film_id'),  
        Index('idx_fk_actor_id', 'actor_id'),  
    )

Base.metadata.create_all(sakila25_engine)
session = Session(sakila25_engine)

language_data = langs()
for iso_code, lang_info in language_data.items():
    lang_info['language_iso_639_1'] = iso_code 
    session.merge(Language(**lang_info))

film_data = topRated_movies()
for film_id, film_info in film_data.items():
    film_info['film_id'] = film_id 
    session.merge(Film(**film_info))

genre_data = genres()
for category_id, category_info in genre_data.items():
    category_info['category_id'] = category_id 
    session.merge(Category(**category_info))

actor_data, film_actor_data = film_actor2()
for actor_id, actor_info in actor_data.items():
    actor_info['actor_id'] = actor_id 
    session.merge(Actor(**actor_info))
for film_actor in film_actor_data:
    session.merge(FilmActor(**film_actor))

film_category_data = filmGenre()
for film_id, film_category_info in film_category_data.items():
    session.merge(FilmCategory(film_id=film_id, 
                               category_id=film_category_info["category_id"]))

session.commit()
