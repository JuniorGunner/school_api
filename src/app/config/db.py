import os
from sqlalchemy import MetaData, create_engine
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)