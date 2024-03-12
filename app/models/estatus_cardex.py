
from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class Estatus_cardexIn(BaseModel):#crear
    estatus: str
    

class Estatus_cardexOut(BaseModel):#obtener
    id: int
    estatus: str
    



class Estatus_cardexInDB(Base):
    __tablename__ = "estatus_cardex"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    estatus = Column(String(50), index=True)