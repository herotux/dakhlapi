from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.income import get_income, create_income
from app.schemas.income import IncomeCreate, IncomeResponse

router = APIRouter()

@router.post("/incomes/", response_model=IncomeResponse)
def create_new_income(income: IncomeCreate, db: Session = Depends(get_db)):
    return create_income(db, income)

@router.get("/incomes/{income_id}", response_model=IncomeResponse)
def read_income(income_id: int, db: Session = Depends(get_db)):
    db_income = get_income(db, income_id)
    if db_income is None:
        raise HTTPException(status_code=404, detail="Income not found")
    return db_income
