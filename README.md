# sakila25
# Overview
This project provides sakila database but with new data for 2025 and small diiffrences, keeping the original flavour of the classic database.

# Restorables
All the databses are restorable using the files in [Sakila25](https://github.com/lilhuss26/sakila25/tree/main/Sakila25)

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="40" alt="PostgreSQL" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="40" alt="MySQL" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" height="40" alt="T-SQL" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="40" alt="SQLite" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="40" alt="MongoDB" />
</p>

- MySQL 
- PostgreSQL
- SQL Server
- MongoDB
- CSV files

Just restore the file in your GUI or terminal

# New schema 
![Sakila25 Schema](https://github.com/lilhuss26/sakila25/raw/main/sakila25_schema.png)

# Creating the databases
- All the databases can be created using the scripts in [scripts]() folder
- Ensure to create a .env file, following the .env.example file
+ TMDB API key is totaly free, you can get it from [TMDB](https://www.themoviedb.org/)
# Project structure
## Fetchers
- Every file in [fetchers]() folder is a script that fetches data from an API 
- Main [FetchData]() call all the fetchers and provide it as one function

## DatabasesCreation
- Every folder in [DatabasesCreation]() folder is responsible for creating a database schema and inserting fetched data
- Main file at each folder call all the databases creation and data insertion scripts and provide it as one function

## Technology 
- `requests` handles fetching data from APIs
- `SQLAlchemy` handles database creation and data insertion
