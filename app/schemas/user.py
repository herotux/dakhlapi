from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: str
    is_admin: bool = False

class UserResponse(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    is_admin: bool
