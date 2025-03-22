from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.person import get_person, create_person
from app.schemas.person import PersonCreate, PersonResponse

router = APIRouter()

@router.post("/persons/", response_model=PersonResponse)
def create_new_person(person: PersonCreate, db: Session = Depends(get_db)):
    return create_person(db, person)

@router.get("/persons/{person_id}", response_model=PersonResponse)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person
