from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class PeriodosIn(BaseModel):
    anio: int
    cat_periodo_id: int

class PeriodosOut(BaseModel):
    id: int
    anio: int
    cat_periodo_id: int

class PeriodosDelete(BaseModel):
    id: int
    
class PeriodosUpdate(BaseModel):
    id: int
    anio: int
    cat_periodo_id: int

class PeriodosInDB(Base):
    __tablename__ = "periodos"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    anio = Column(Integer, nullable=False)
    cat_periodo_id = Column(Integer, ForeignKey('cat_periodos.id'))  # Clave foránea
    
    cat_periodos = relationship("Cat_periodosInDB", back_populates="periodos")  # Relación inversa con personas
