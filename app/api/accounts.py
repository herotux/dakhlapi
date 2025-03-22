from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.account import get_account, create_account
from app.schemas.account import AccountCreate, AccountResponse

router = APIRouter()

@router.post("/accounts/", response_model=AccountResponse)
def create_new_account(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@router.get("/accounts/{account_id}", response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = get_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account
