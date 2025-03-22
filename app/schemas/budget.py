from pydantic import BaseModel

class BudgetCreate(BaseModel):
    user_id: int
    monthly_budget: int
    category_id: int

class BudgetResponse(BaseModel):
    id: int
    user_id: int
    monthly_budget: int
    category_id: int
