# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Category Routes
@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/foods/", response_model=list[schemas.Food])
def read_foods(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    foods = crud.get_foods(db=db)
    return foods

@app.post("/foods/", response_model=schemas.Food)
def create_food(food: schemas.FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db=db, food=food)

# User Routes
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/login/", response_model=schemas.User)
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.verify_user(db=db, email=user_login.email, password=user_login.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

# Doctor Test Routes
@app.post("/doctor_tests/", response_model=schemas.DoctorTest)
def create_doctor_test(doctor_test: schemas.DoctorTestCreate, db: Session = Depends(get_db)):
    return crud.create_doctor_test(db=db, doctor_test=doctor_test)

@app.get("/doctor_tests/user/{user_id}", response_model=list[schemas.DoctorTest])
def read_doctor_tests(user_id: int, db: Session = Depends(get_db)):
    return crud.get_doctor_tests_by_user(db=db, user_id=user_id)
