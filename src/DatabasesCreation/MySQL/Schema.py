from sqlalchemy import Index
from sqlalchemy import (SmallInteger,Boolean, DateTime,TEXT,
                        Column, DECIMAL,VARCHAR, Integer, String, ForeignKey, BigInteger)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql import text
from src.DatabasesCreation.MySQL.configuration import sakila25_engine


Base = declarative_base()


class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(255))
    rating = Column(DECIMAL(4, 3))
    description = Column(TEXT)
    release_date = Column(DateTime)
    language_iso_639_1 = Column(VARCHAR(3), ForeignKey('language.language_iso_639_1'))
    popularity = Column(DECIMAL(8, 4))
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
    language_iso_639_1 = Column(VARCHAR(3), primary_key=True)
    english_name = Column(VARCHAR(10))
    name = Column(VARCHAR(10))


class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))

    __table_args__ = (
        Index('idx_actor_last_name', 'last_name'),
    )


class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer, ForeignKey('actor.actor_id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    character = Column(TEXT)
    __table_args__ = (
        Index('idx_fk_film_id', 'film_id'),
        Index('idx_fk_actor_id', 'actor_id'),
    )
    
Base.metadata.create_all(sakila25_engine)

