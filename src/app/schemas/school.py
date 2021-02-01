from pydantic import BaseModel


class SchoolSchema(BaseModel):
    name: str


class SchoolDB(SchoolSchema):
    id: int