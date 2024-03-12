from sqlalchemy import Column, BigInteger, String, ForeignKey
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class DocentesIn(BaseModel):#crear
    persona_id: int
    

class DocentesOut(BaseModel):#obtener
    id: int
    persona_id: int


class DocentesInDB(Base):
    __tablename__ = "docentes"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    persona_id = Column(BigInteger, ForeignKey('personas.id'))  # Clave foránea