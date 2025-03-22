from sqlalchemy.orm import Session
from app.models.budget import Budget
from app.schemas.budget import BudgetCreate

def get_budget(db: Session, budget_id: int):
    return db.query(Budget).filter(Budget.id == budget_id).first()

def create_budget(db: Session, budget: BudgetCreate):
    db_budget = Budget(**budget.dict())
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget
