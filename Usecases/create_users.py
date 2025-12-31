from src.FetchData.Fetchers.users import fetch_users
from src.DatabasesCreation.MySQL.insertion import mysql_insert_users_data

print("Starting User Data Insertion...")

# 1. Fetch only user data
print("Fetching user data...")
countries, cities, addresses, customers = fetch_users()

# 2. Insert into MySQL
print("Inserting into database...")
mysql_insert_users_data(countries, cities, addresses, customers)

print("Done!")
