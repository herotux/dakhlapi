from pydantic import BaseModel
from typing import List, Optional

class InstallmentCreate(BaseModel):
    user_id: int
    person_id: int
    amount: int
    text: str
    inst_num: int
    inst_rate: float
    first_date: str
    pay_period: int

class InstallmentDetailCreate(BaseModel):
    installment_id: int
    inst_num: int
    payment_status: str
    payment_date: str
    amount: int

class InstallmentResponse(BaseModel):
    id: int
    user_id: int
    person_id: int
    amount: int
    text: str
    inst_num: int
    inst_rate: float
    first_date: str
    pay_period: int
    installment_details: List[InstallmentDetailCreate]

class InstallmentDetailResponse(BaseModel):
    id: int
    installment_id: int
    inst_num: int
    payment_status: str
    payment_date: str
    amount: int
