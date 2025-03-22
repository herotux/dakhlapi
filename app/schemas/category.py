from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    user_id: int
    parent_id: int = None
    is_income: bool = False

class CategoryResponse(BaseModel):
    id: int
    name: str
    user_id: int
    parent_id: int = None
    is_income: bool
