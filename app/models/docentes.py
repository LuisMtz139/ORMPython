from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from app.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship


from typing import Optional

class DocentesIn(BaseModel):#crear
    persona_id: int
    

class DocentesOut(BaseModel):#obtener
    id: int
    persona_id: int


class DocentesInDB(Base):
    __tablename__ = "docentes"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    
    
    persona_id = Column(Integer, ForeignKey('personas.id'))
    persona = relationship("PersonasInDB", back_populates="docentes")