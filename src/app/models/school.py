import os
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

schools = Table(
    "schools",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100))
)

# schools.drop(engine)
# schools.__table__.drop()
# database = Database(DATABASE_URL)
metadata.create_all(engine)