from sqlalchemy import select, func, literal_column
from sqlalchemy.schema import DDL
from src.DatabasesCreation.PostgreSQL.configuration import sakila25_engine
from src.DatabasesCreation.PostgreSQL.schema import (Actor, Film, FilmActor, FilmCategory, Category,
                                                      Customer, Address, City, Country,
                                                      Payment, Subscription, Inventory, Provider)


def create_views():
    with sakila25_engine.connect() as conn:
        conn.execute(DDL("DROP VIEW IF EXISTS actor_info"))

        actor_info_select = select(
            Actor.actor_id,
            Actor.first_name,
            Actor.last_name,
            func.string_agg(
                Film.title.distinct(), ', '
            ).label('film_info')
        ).select_from(
            Actor.__table__.outerjoin(FilmActor, Actor.actor_id == FilmActor.actor_id)
            .outerjoin(Film, FilmActor.film_id == Film.film_id)
        ).group_by(
            Actor.actor_id,
            Actor.first_name,
            Actor.last_name
        )

        create_actor_info = DDL(
            f"CREATE VIEW actor_info AS {actor_info_select.compile(sakila25_engine, compile_kwargs={'literal_binds': True})}"
        )
        conn.execute(create_actor_info)

        conn.execute(DDL("DROP VIEW IF EXISTS customer_list"))

        customer_list_select = select(
            Customer.customer_id.label('ID'),
            func.concat(Customer.first_name, ' ', Customer.last_name).label('name'),
            Address.address,
            Address.postal_code.label('zip_code'),
            City.city,
            Country.country,
            Customer.provider_id.label('SID')
        ).select_from(
            Customer.__table__.outerjoin(Address, Customer.address_id == Address.address_id)
            .outerjoin(City, Address.city_id == City.city_id)
            .outerjoin(Country, City.country_id == Country.country_id)
        )

        create_customer_list = DDL(
            f"CREATE VIEW customer_list AS {customer_list_select.compile(sakila25_engine, compile_kwargs={'literal_binds': True})}"
        )
        conn.execute(create_customer_list)

        conn.execute(DDL("DROP VIEW IF EXISTS film_list"))

        film_list_select = select(
            Film.film_id.label('FID'),
            Film.title,
            Film.description,
            Category.name.label('category'),
            Film.runtime.label('length'),
            Film.rating,
            func.string_agg(
                func.concat(Actor.first_name, ' ', Actor.last_name).distinct(), ', '
            ).label('actors')
        ).select_from(
            Film.__table__.outerjoin(FilmCategory, Film.film_id == FilmCategory.film_id)
            .outerjoin(Category, FilmCategory.category_id == Category.category_id)
            .outerjoin(FilmActor, Film.film_id == FilmActor.film_id)
            .outerjoin(Actor, FilmActor.actor_id == Actor.actor_id)
        ).group_by(
            Film.film_id,
            Film.title,
            Film.description,
            Category.name,
            Film.runtime,
            Film.rating
        )

        create_film_list = DDL(
            f"CREATE VIEW film_list AS {film_list_select.compile(sakila25_engine, compile_kwargs={'literal_binds': True})}"
        )
        conn.execute(create_film_list)

        conn.execute(DDL("DROP VIEW IF EXISTS revenue_by_provider"))

        revenue_by_provider_select = select(
            Provider.provider_name.label('provider'),
            func.sum(Payment.amount).label('total_sales')
        ).select_from(
            Payment.__table__.join(Subscription, Payment.subscription_id == Subscription.subscription_id)
            .join(Inventory, Subscription.inventory_id == Inventory.inventory_id)
            .join(Provider, Inventory.provider_id == Provider.provider_id)
        ).group_by(
            Provider.provider_id,
            Provider.provider_name
        ).order_by(
            literal_column('total_sales').desc()
        )

        create_revenue_by_provider = DDL(
            f"CREATE VIEW revenue_by_provider AS {revenue_by_provider_select.compile(sakila25_engine, compile_kwargs={'literal_binds': True})}"
        )
        conn.execute(create_revenue_by_provider)

        conn.commit()
        print("Views created successfully")
