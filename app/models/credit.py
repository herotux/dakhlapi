from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Credit(Base):
    __tablename__ = "credits"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    person_id = Column(Integer, ForeignKey("persons.id"))
    amount = Column(Integer)
    text = Column(String)
    date = Column(String)
    pay_date = Column(String)
