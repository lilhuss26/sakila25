from sqlalchemy import select, func, literal_column
from sqlalchemy.schema import DDL
from src.DatabasesCreation.SQLServer.configuration import sakila25_engine
from src.DatabasesCreation.SQLServer.schema import (Actor, Film, FilmActor, FilmCategory, Category,
                                                     Customer, Address, City, Country,
                                                     Payment, Subscription, Inventory, Provider)


def create_views():
    with sakila25_engine.connect() as conn:
        conn.execute(DDL("DROP VIEW IF EXISTS actor_info"))

        conn.execute(DDL("""
            CREATE VIEW actor_info AS
            SELECT 
                a.actor_id,
                a.first_name,
                a.last_name,
                STRING_AGG(f.title, ', ') WITHIN GROUP (ORDER BY f.title) AS film_info
            FROM actor a
            LEFT OUTER JOIN film_actor fa ON a.actor_id = fa.actor_id
            LEFT OUTER JOIN film f ON fa.film_id = f.film_id
            GROUP BY a.actor_id, a.first_name, a.last_name
        """))

        conn.execute(DDL("DROP VIEW IF EXISTS customer_list"))

        conn.execute(DDL("""
            CREATE VIEW customer_list AS
            SELECT 
                c.customer_id AS ID,
                CONCAT(c.first_name, ' ', c.last_name) AS name,
                a.address,
                a.postal_code AS zip_code,
                ci.city,
                co.country,
                c.provider_id AS SID
            FROM customer c
            LEFT OUTER JOIN address a ON c.address_id = a.address_id
            LEFT OUTER JOIN city ci ON a.city_id = ci.city_id
            LEFT OUTER JOIN country co ON ci.country_id = co.country_id
        """))

        conn.execute(DDL("DROP VIEW IF EXISTS film_list"))

        conn.execute(DDL("""
            CREATE VIEW film_list AS
            SELECT 
                f.film_id AS FID,
                f.title,
                CAST(f.description AS VARCHAR(MAX)) AS description,
                c.name AS category,
                f.runtime AS length,
                f.rating,
                STRING_AGG(CONCAT(a.first_name, ' ', a.last_name), ', ') WITHIN GROUP (ORDER BY a.last_name) AS actors
            FROM film f
            LEFT OUTER JOIN film_category fc ON f.film_id = fc.film_id
            LEFT OUTER JOIN category c ON fc.category_id = c.category_id
            LEFT OUTER JOIN film_actor fa ON f.film_id = fa.film_id
            LEFT OUTER JOIN actor a ON fa.actor_id = a.actor_id
            GROUP BY f.film_id, f.title, CAST(f.description AS VARCHAR(MAX)), c.name, f.runtime, f.rating
        """))

        conn.execute(DDL("DROP VIEW IF EXISTS revenue_by_provider"))

        conn.execute(DDL("""
            CREATE VIEW revenue_by_provider AS
            SELECT 
                pr.provider_name AS provider,
                SUM(p.amount) AS total_sales
            FROM payment p
            INNER JOIN subscription s ON p.subscription_id = s.subscription_id
            INNER JOIN inventory i ON s.inventory_id = i.inventory_id
            INNER JOIN provider pr ON i.provider_id = pr.provider_id
            GROUP BY pr.provider_id, pr.provider_name
        """))

        conn.commit()
        print("Views created successfully")
