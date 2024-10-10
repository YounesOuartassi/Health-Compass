# app/schemas.py
from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class FoodBase(BaseModel):
    name: str
    category_id: Optional[int] = None
    nutrition_grade: Optional[str] = None
    calories: Optional[int] = None

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
# User Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Doctor Test Schemas
class DoctorTestBase(BaseModel):
    user_id: int
    test_date: date
    file_path: str

class DoctorTestCreate(DoctorTestBase):
    pass

class DoctorTest(DoctorTestBase):
    id: int

    class Config:
        orm_mode = True