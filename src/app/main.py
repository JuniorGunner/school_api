from fastapi import FastAPI
from app.config.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# @app.get("/ping")
# def pong():
#     return {"ping": "pong!"}