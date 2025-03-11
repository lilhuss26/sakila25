import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
connection_string = os.getenv('MYSQL_STRING')

engine = create_engine(connection_string)
Base = automap_base()

Base.prepare(autoload_with=engine)
LaptopPrices = Base.classes.laptop_prices

session = Session(engine)

laptops = session.query(LaptopPrices).all()
for laptop in laptops[:10]:
    print(f"{laptop.laptop_ID}  {laptop.Company}")
session.close()