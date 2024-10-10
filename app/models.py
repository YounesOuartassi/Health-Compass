# app/models.py
from sqlalchemy import Column, BigInteger, String, Date, ForeignKey, Integer, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

class DoctorTest(Base):
    __tablename__ = "doctor_tests"
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    test_date = Column(Date, nullable=False)
    file_path = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class Food(Base):
    __tablename__ = "foods"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category_id = Column(BigInteger, ForeignKey("categories.id"), nullable=True)
    nutrition_grade = Column(String(5), nullable=True)
    calories = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class UserFood(Base):
    __tablename__ = "user_foods"
    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    food_id = Column(BigInteger, ForeignKey("foods.id"), nullable=True)
    consumed_at = Column(TIMESTAMP, nullable=False)



