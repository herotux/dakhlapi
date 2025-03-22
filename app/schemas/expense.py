from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    user_id: int
    amount: int
    date: str
    text: str
    category_id: int

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    amount: int
    date: str
    text: str
    category_id: int
