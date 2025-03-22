from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    amount: int
    user_id: int

class AccountResponse(BaseModel):
    id: int
    name: str
    amount: int
    user_id: int
