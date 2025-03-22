from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.category import get_category, create_category
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)

@router.get("/categories/{category_id}", response_model=CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
