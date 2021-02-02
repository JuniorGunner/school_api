from app.schemas.school import SchoolSchema
from app.models.school import schools
from app.config.db import database


async def post(payload: SchoolSchema):
    query = schools.insert().values(name=payload.name)
    return await database.execute(query=query)


async def get(id: int):
    query = schools.select().where(id == schools.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = schools.select()
    return await database.fetch_all(query=query)


async def put(id: int , payload: SchoolSchema):
    query =  (
        schools
        .update()
        .where(id == schools.c.id)
        .values(name=payload.name)
        .returning(schools.c.id)
    )
    return await database.execute(query=query)