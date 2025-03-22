from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.expense import get_expense, create_expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse

router = APIRouter()

@router.post("/expenses/", response_model=ExpenseResponse)
def create_new_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense)

@router.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = get_expense(db, expense_id)
    if db_expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return db_expense
