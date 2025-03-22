from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.installment import get_installment, create_installment
from app.schemas.installment import InstallmentCreate, InstallmentResponse

router = APIRouter()

@router.post("/installments/", response_model=InstallmentResponse)
def create_new_installment(installment: InstallmentCreate, db: Session = Depends(get_db)):
    return create_installment(db, installment)

@router.get("/installments/{installment_id}", response_model=InstallmentResponse)
def read_installment(installment_id: int, db: Session = Depends(get_db)):
    db_installment = get_installment(db, installment_id)
    if db_installment is None:
        raise HTTPException(status_code=404, detail="Installment not found")
    return db_installment
