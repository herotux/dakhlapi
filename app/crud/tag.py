from sqlalchemy.orm import Session
from app.models.tag import Tag
from app.schemas.tag import TagCreate

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
