from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserPublic(BaseModel):
    username: str
    email: EmailStr