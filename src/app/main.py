from fastapi import FastAPI
from app.config.db import database, engine, metadata
from app.routers import school

# TODO: Check tables creation via main.py - bug;
# metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(school.router, prefix="/schools", tags=["schools"])