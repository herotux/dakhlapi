from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate

def get_account(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account: AccountCreate):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account
