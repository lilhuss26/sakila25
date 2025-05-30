import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import SmallInteger,Boolean, DateTime,TEXT,Column, DECIMAL,VARCHAR, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TINYINT

load_dotenv()
connection_string = os.getenv('MYSQL_STRING')

engine = create_engine(connection_string)
Base = declarative_base()

class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer,primary_key=True)
    title = Column(VARCHAR(255))
    rating = Column(DECIMAL(4,3))
    description = Column(TEXT)
    release_date = Column(DateTime)
    language_iso_639_1 = Column(VARCHAR(3), ForeignKey('language.iso_639_1'))
    popularity = Column(DECIMAL(6,4))
    revenue = Column(Integer)
    runtime = Column(SmallInteger)
    adult = Column(Boolean)

class FilmCategory(Base):
    __tablename__ = 'film_category'
    film_id = Column(Integer, ForeignKey('film.film_id'))
    category_id = Column(TINYINT, ForeignKey('category.category_id'))

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(25))

class Language(Base):
    __tablename__ = 'language'
    language_iso_639_1 = Column(VARCHAR(3),primary_key=True)
    english_name = Column(VARCHAR(10))
    name = Column(VARCHAR(10))

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(SmallInteger,primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    
class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(SmallInteger,ForeignKey('actor.actor_id'))
    film_id = Column(Integer, ForeignKey('film.film_id'))