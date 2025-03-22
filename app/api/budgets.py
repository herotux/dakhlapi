from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.budget import get_budget, create_budget
from app.schemas.budget import BudgetCreate, BudgetResponse

router = APIRouter()

@router.post("/budgets/", response_model=BudgetResponse)
def create_new_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    return create_budget(db, budget)

@router.get("/budgets/{budget_id}", response_model=BudgetResponse)
def read_budget(budget_id: int, db: Session = Depends(get_db)):
    db_budget = get_budget(db, budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return db_budget
