from pydantic import BaseModel

class PersonCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    relation: str

class PersonResponse(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    relation: str
