from pydantic import BaseModel

class TagCreate(BaseModel):
    user_id: int
    name: str
    description: str

class TagResponse(BaseModel):
    id: int
    user_id: int
    name: str
    description: str
