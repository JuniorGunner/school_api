from app.services import school
from app.schemas.school import SchoolDB, SchoolSchema
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()


@router.post("/", response_model=SchoolDB, status_code=201)
async def create_school(payload: SchoolSchema):
    school_id = await school.post(payload)

    response_object = {
        "id": school_id,
        "name": payload.name
    }

    return response_object


@router.get("/{id}", response_model=SchoolDB)
async def read_school(id: int):
    school_data = await school.get(id)
    if not school_data:
        raise HTTPException(status_code=404, detail="School not found")
    return school_data


@router.get("/", response_model=List[SchoolDB])
async def read_all_schools():
    return await school.get_all()