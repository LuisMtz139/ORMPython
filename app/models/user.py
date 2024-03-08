from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class UserIn(BaseModel):#crear
    full_name: str
    phone: str
    password: str

class UserOut(BaseModel):#obtener
    id: int
    full_name: str
    phone: str
    password: str
    

class UserDelete(BaseModel):
    id: int
    
class UserUpdate(BaseModel):
    id: int
    full_name: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None

class UserInDB(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(50), index=True)
    phone = Column(String(10),  index=True)  #unique=True
    password = Column(String(100))