from pydantic import BaseModel

class CreditCreate(BaseModel):
    user_id: int
    person_id: int
    amount: int
    text: str
    date: str
    pay_date: str

class CreditResponse(BaseModel):
    id: int
    user_id: int
    person_id: int
    amount: int
    text: str
    date: str
    pay_date: str
