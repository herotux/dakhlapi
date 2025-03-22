from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Installment(Base):
    __tablename__ = "installments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    person_id = Column(Integer, ForeignKey("persons.id"))
    amount = Column(Integer)
    text = Column(String)
    inst_num = Column(Integer)
    inst_rate = Column(Float)
    first_date = Column(String)
    pay_period = Column(Integer)
    installment_details = relationship("InstallmentDetail", back_populates="installment")

class InstallmentDetail(Base):
    __tablename__ = "installment_details"
    id = Column(Integer, primary_key=True, index=True)
    installment_id = Column(Integer, ForeignKey("installments.id"))
    inst_num = Column(Integer)
    payment_status = Column(String)
    payment_date = Column(String)
    amount = Column(Integer)
    installment = relationship("Installment", back_populates="installment_details")
