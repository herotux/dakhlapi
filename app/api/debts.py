from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.debt import get_debt, create_debt
from app.schemas.debt import DebtCreate, DebtResponse

router = APIRouter()

@router.post("/debts/", response_model=DebtResponse)
def create_new_debt(debt: DebtCreate, db: Session = Depends(get_db)):
    return create_debt(db, debt)

@router.get("/debts/{debt_id}", response_model=DebtResponse)
def read_debt(debt_id: int, db: Session = Depends(get_db)):
    db_debt = get_debt(db, debt_id)
    if db_debt is None:
        raise HTTPException(status_code=404, detail="Debt not found")
    return db_debt
