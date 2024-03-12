from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel


from typing import Optional

class DocentesIn(BaseModel):#crear
    persona_id: int
    

class DocentesOut(BaseModel):#obtener
    id: int


class DocentesInDB(Base):
    __tablename__ = "docentes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    
    

#FOREIGN KEY (persona_id) REFERENCES personas(id)

