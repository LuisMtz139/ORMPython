from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class AsignaturasIn(BaseModel):#crear
    nombre: str
    creditos: int
    cuatrimestre: str
    plan_id: int

class AsignaturasOut(BaseModel):#obtener
    id: int
    nombre: str
    creditos: int
    cuatrimestre: str
    plan_id: int

class AsignaturasInDB(Base):
    __tablename__ = "asignaturas"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True)
    creditos = Column(Integer, index=True)
    cuatrimestre = Column(String(50), index=True)
    plan_id = Column(BigInteger, ForeignKey('planes.id'))  # Clave foránea