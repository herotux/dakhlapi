from sqlalchemy.orm import Session
from app.models.installment import Installment, InstallmentDetail
from app.schemas.installment import InstallmentCreate, InstallmentDetailCreate
from datetime import datetime, timedelta
import math

def calculate_installment(amount: int, rate: float, inst_num: int) -> float:
    """
    محاسبه مبلغ هر قسط با توجه به مبلغ کل، نرخ بهره، و تعداد اقساط.
    فرمول: (قسط = (مبلغ کل * نرخ بهره / 1200) / (1 - (1 + نرخ بهره / 1200)^(-تعداد اقساط))
    """
    monthly_rate = rate / 1200
    installment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** (-inst_num))
    return round(installment)

def create_installment(db: Session, installment: InstallmentCreate):
    # ایجاد وام جدید
    db_installment = Installment(**installment.dict())
    db.add(db_installment)
    db.commit()
    db.refresh(db_installment)

    # محاسبه جزئیات اقساط
    installment_amount = calculate_installment(
        installment.amount, installment.inst_rate, installment.inst_num
    )
    first_date = datetime.strptime(installment.first_date, "%Y-%m-%d")

    for i in range(1, installment.inst_num + 1):
        payment_date = first_date + timedelta(days=30 * i)
        installment_detail = InstallmentDetail(
            installment_id=db_installment.id,
            inst_num=i,
            payment_status="unpaid",
            payment_date=payment_date.strftime("%Y-%m-%d"),
            amount=installment_amount,
        )
        db.add(installment_detail)

    db.commit()
    db.refresh(db_installment)
    return db_installment

def get_installment(db: Session, installment_id: int):
    return db.query(Installment).filter(Installment.id == installment_id).first()
