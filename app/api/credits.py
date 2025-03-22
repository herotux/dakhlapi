from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.credit import get_credit, create_credit
from app.schemas.credit import CreditCreate, CreditResponse

router = APIRouter()

@router.post("/credits/", response_model=CreditResponse)
def create_new_credit(credit: CreditCreate, db: Session = Depends(get_db)):
    return create_credit(db, credit)

@router.get("/credits/{credit_id}", response_model=CreditResponse)
def read_credit(credit_id: int, db: Session = Depends(get_db)):
    db_credit = get_credit(db, credit_id)
    if db_credit is None:
        raise HTTPException(status_code=404, detail="Credit not found")
    return db_credit
