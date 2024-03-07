# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

class UserBase(BaseModel):
    full_name: str
    phone: str
    curp: str

class UserCreate(UserBase):
    password: str

class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), unique=True, index=True)
    phone = Column(String(10), unique=True, index=True)  
    password = Column(String(100))

class User(UserBase):
    id: int