from sqlalchemy.orm import Session
from app.models.credit import Credit
from app.schemas.credit import CreditCreate

def get_credit(db: Session, credit_id: int):
    return db.query(Credit).filter(Credit.id == credit_id).first()

def create_credit(db: Session, credit: CreditCreate):
    db_credit = Credit(**credit.dict())
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit
