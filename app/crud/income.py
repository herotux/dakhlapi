from sqlalchemy.orm import Session
from app.models.income import Income
from app.schemas.income import IncomeCreate

def get_income(db: Session, income_id: int):
    return db.query(Income).filter(Income.id == income_id).first()

def create_income(db: Session, income: IncomeCreate):
    db_income = Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income
