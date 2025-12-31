from sqlalchemy import Index
from sqlalchemy import (SmallInteger,Boolean, DateTime,TEXT,
                        Column, DECIMAL,VARCHAR, Integer, CHAR, ForeignKey, BigInteger, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
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
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_title', 'title'),
        Index('idx_fk_language_id', 'language_iso_639_1'),
    )


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(25))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class FilmCategory(Base):
    __tablename__ = 'film_category'
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'), primary_key=True)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_fk_film_id', 'film_id'),
        Index('idx_fk_category_id', 'category_id'),
    )


class Language(Base):
    __tablename__ = 'language'
    language_iso_639_1 = Column(VARCHAR(3), primary_key=True)
    english_name = Column(VARCHAR(10))
    name = Column(VARCHAR(10))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Actor(Base):
    __tablename__ = 'actor'
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_actor_last_name', 'last_name'),
    )


class FilmActor(Base):
    __tablename__ = 'film_actor'
    actor_id = Column(Integer, ForeignKey('actor.actor_id'), primary_key=True)
    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    character = Column(TEXT)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    __table_args__ = (
        Index('idx_fk_film_id', 'film_id'),
        Index('idx_fk_actor_id', 'actor_id'),
    )

class Provider(Base):
    __tablename__ = 'provider'
    provider_id = Column(Integer, primary_key=True)
    provider_name = Column(VARCHAR(255))
    type = Column(VARCHAR(255))
    country = Column(VARCHAR(255))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.film_id'))
    provider_id = Column(Integer, ForeignKey('provider.provider_id'))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(VARCHAR(100))
    country_slag = Column(VARCHAR(2))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(VARCHAR(100))
    country_id = Column(Integer, ForeignKey('country.country_id'))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Address(Base):
    __tablename__ = 'address'
    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(VARCHAR(255))
    address2 = Column(VARCHAR(255))
    state = Column(VARCHAR(100))
    city_id = Column(Integer, ForeignKey('city.city_id'))
    postal_code = Column(VARCHAR(20))
    offset = Column(VARCHAR(20))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(VARCHAR(36), primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    email = Column(VARCHAR(100))
    address_id = Column(Integer, ForeignKey('address.address_id'))
    active = Column(Boolean)
    create_date = Column(DateTime)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    provider_id = Column(Integer, ForeignKey('provider.provider_id'))
    date_of_birth = Column(DateTime)
    gender = Column(VARCHAR(10))

class Cards(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(VARCHAR(36), ForeignKey('customer.customer_id'))
    card_number = Column(VARCHAR(255))
    card_type = Column(VARCHAR(255))
    card_expiry_date = Column(CHAR(5))
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Subscription(Base):
    __tablename__ = 'subscription'
    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(VARCHAR(36), ForeignKey('customer.customer_id'))
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    type = Column(VARCHAR(255))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

class Payment(Base):
    __tablename__ = 'payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(VARCHAR(36), ForeignKey('customer.customer_id'))
    subscription_id = Column(Integer, ForeignKey('subscription.subscription_id'))
    card_id = Column(Integer, ForeignKey('cards.card_id'))
    amount = Column(DECIMAL(10, 2))
    payment_date = Column(DateTime)
    last_update = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

Base.metadata.create_all(sakila25_engine)

