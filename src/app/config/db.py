import os
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy.sql import func
from databases import Database

# TODO: Check engine, metadata and database ceration and imports;

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)