from sqlalchemy.orm import Session
from app.models.debt import Debt
from app.schemas.debt import DebtCreate

def get_debt(db: Session, debt_id: int):
    return db.query(Debt).filter(Debt.id == debt_id).first()

def create_debt(db: Session, debt: DebtCreate):
    db_debt = Debt(**debt.dict())
    db.add(db_debt)
    db.commit()
    db.refresh(db_debt)
    return db_debt
