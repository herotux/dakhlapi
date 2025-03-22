from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.tag import get_tag, create_tag
from app.schemas.tag import TagCreate, TagResponse

router = APIRouter()

@router.post("/tags/", response_model=TagResponse)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@router.get("/tags/{tag_id}", response_model=TagResponse)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag
