from pydantic import BaseModel

class IncomeCreate(BaseModel):
    user_id: int
    amount: int
    date: str
    text: str
    category_id: int

class IncomeResponse(BaseModel):
    id: int
    user_id: int
    amount: int
    date: str
    text: str
    category_id: int
