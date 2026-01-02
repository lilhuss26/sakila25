# Sakila25

A modernized version of the classic Sakila database with 2025 data, supporting multiple database platforms.

## Features
- 🎬 Real movie data from TMDB API
- 💳 Realistic customer and payment data
- 🗄️ Multi-database support: MySQL, PostgreSQL, SQL Server, MongoDB
- 📊 CSV exports for data analysis
- 🔄 Fully reproducible with Python scripts

## Supported Databases

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="40" alt="MySQL" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="40" alt="PostgreSQL" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" height="40" alt="SQL Server" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="40" alt="MongoDB" />
</p>

- [MySQL](https://github.com/lilhuss26/sakila25/tree/main/Sakila25/MySQL)
- [PostgreSQL](https://github.com/lilhuss26/sakila25/tree/main/Sakila25/PostgreSQL)
- [SQL Server](https://github.com/lilhuss26/sakila25/tree/main/Sakila25/SQLServer)
- [MongoDB](https://github.com/lilhuss26/sakila25/tree/main/Sakila25/MongoDB/sakila25)
- [CSV files](https://github.com/lilhuss26/sakila25/tree/main/Sakila25/Sakila25_csv)
## Pre-built Database Backups

Ready-to-use database dumps are available in the `Sakila25/` folder. Simply restore them using your preferred database tool:

```bash
# MySQL
mysql -u username -p sakila25 < Sakila25/sakila25_mysql.sql

# PostgreSQL
psql -U username -d sakila25 -f Sakila25/sakila25_postgresql.sql

# SQL Server
sqlcmd -S localhost -d sakila25 -i Sakila25/sakila25_sqlserver.sql
```

## Database Schema

![Sakila25 Schema](sakila25_schema.png)

The schema includes:
- **Films** with actors, categories, and languages
- **Customers** with addresses and payment cards
- **Providers** (streaming services) with inventory
- **Subscriptions** and **Payments**
- **Views** for common queries (actor_info, customer_list, film_list, revenue_by_provider)

## Differences from Original Sakila

- ✅ Modern 2025 movie data
- ✅ Streaming providers instead of rental stores
- ✅ Subscription-based model with payments
- ✅ Credit card information
- ✅ Multi-database support including NoSQL
- ✅ Automated data generation from APIs
## Prerequisites

- **Python 3.12+**
- **Database Server** (one or more):
  - MySQL 8.0+
  - PostgreSQL 13+
  - SQL Server 2019+
  - MongoDB 5.0+
- **TMDB API Key** - Free from [themoviedb.org](https://www.themoviedb.org/settings/api)

## Quick Start

### 1. Installation

```bash
git clone https://github.com/lilhuss26/sakila25.git
cd sakila25
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file based on `.env.example`:

```env
TMDB_API_KEY="your_tmdb_api_key"
TMDB_TOKEN="your_tmdb_token"
MYSQL_STRING="mysql+pymysql://username:password@localhost:3306"
POSTGRESQL_STRING="postgresql+psycopg2://username:password@localhost:5432/sakila25"
SQLSERVER_STRING="mssql+pymssql://username:password@localhost:1433/sakila25"
MONGODB_STRING="mongodb://username:password@localhost:27017/"
```

### 3. Create Databases

**Important:** For PostgreSQL and SQL Server, create the database first:

```sql
-- PostgreSQL
CREATE DATABASE sakila25;

-- SQL Server
CREATE DATABASE sakila25;
```

Then run the creation scripts:

```bash
# MySQL (auto-creates database)
python scripts/create_mysql.py

# PostgreSQL
python scripts/create_postgresql.py

# SQL Server
python scripts/create_sqlserver.py

# MongoDB (auto-creates database)
python scripts/create_mongodb.py

# Generate CSV files
python scripts/create_csv.py
```


## Project Structure

```
sakila25/
├── src/
│   ├── FetchData/              # API data fetchers
│   │   ├── Fetchers/           # Individual fetcher modules
│   │   └── FetchData.py        # Main fetcher orchestrator
│   └── DatabasesCreation/      # Database implementations
│       ├── MySQL/              # MySQL schema, insertion, views
│       ├── PostgreSQL/         # PostgreSQL schema, insertion, views
│       ├── SQLServer/          # SQL Server schema, insertion, views
│       ├── MongoDB/            # MongoDB denormalized structure
│       └── CSV/                # CSV export functionality
├── scripts/                    # Database creation scripts
├── Sakila25/                   # Pre-built database backups
└── .env.example                # Environment configuration template
```

## Technology Stack

- **SQLAlchemy** - ORM and schema management
- **pymongo** - MongoDB driver
- **pymssql** - SQL Server drivers
- **psycopg2** - PostgreSQL driver
- **pymysql** - MySQL driver
- **requests** - API data fetching
- **pandas** - CSV generation
- **python-dotenv** - Environment configuration

## Data Sources

- **Movies & Actors**: [The Movie Database (TMDB) API](https://www.themoviedb.org/)
- **Customers**: [Random User Generator API](https://randomuser.me/)
- **Credit Cards**: [Faker API](https://fakerapi.it/)

## MongoDB Structure

MongoDB uses a **denormalized** structure for optimal performance:

- **films** collection: Embedded actors, categories, and language
- **providers** collection: Embedded inventory
- **customers** collection: Embedded address, card, subscriptions, and payments



## Troubleshooting

### Connection Issues
- Ensure database servers are running
- Verify connection strings in `.env`
- Check firewall settings

### SQL Server Views Error
- SQL Server doesn't support `ORDER BY` in views without `TOP`
- Views are created without ordering; add `ORDER BY` when querying

### MongoDB Connection
- MongoDB doesn't require database creation beforehand
- Database is created automatically on first insert

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
