from pydantic import BaseModel

class DebtCreate(BaseModel):
    user_id: int
    person_id: int
    amount: int
    text: str
    date: str
    pay_date: str

class DebtResponse(BaseModel):
    id: int
    user_id: int
    person_id: int
    amount: int
    text: str
    date: str
    pay_date: str
