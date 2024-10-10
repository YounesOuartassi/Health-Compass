# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_foods(db: Session):
    return db.query(models.Food).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)  # Hash the password before storing it
    db_user = models.User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def verify_user(db: Session, email: str, password: str):
    user = get_user_by_email(db=db, email=email)
    if user and pwd_context.verify(password, user.password):
        return user
    return None
# Doctor Test CRUD operations
def create_doctor_test(db: Session, doctor_test: schemas.DoctorTestCreate):
    db_doctor_test = models.DoctorTest(**doctor_test.dict())
    db.add(db_doctor_test)
    db.commit()
    db.refresh(db_doctor_test)
    return db_doctor_test

def get_doctor_tests_by_user(db: Session, user_id: int):
    return db.query(models.DoctorTest).filter(models.DoctorTest.user_id == user_id).all()
