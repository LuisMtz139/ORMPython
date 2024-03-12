from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel

class GruposIn(BaseModel):
    periodo_id: int
    asignatura_id: int
    docente_id: int

class GruposOut(BaseModel):
    id: int
    periodo_id: int
    asignatura_id: int
    docente_id: int

class GruposDelete(BaseModel):
    id: int
    
class GruposUpdate(BaseModel):
    id: int
    periodo_id: int
    asignatura_id: int
    docente_id: int

class GruposInDB(Base):
    __tablename__ = "grupos"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    """periodo_id = Column(BigInteger, ForeignKey("periodos.id"))
    asignatura_id = Column(BigInteger, ForeignKey("asignaturas.id"))
    docente_id = Column(BigInteger, ForeignKey("docentes.id"))

    # Relaciones
    periodo = relationship("PeriodosInDB", back_populates="grupos")
    asignatura = relationship("AsignaturasInDB", back_populates="grupos")
    docente = relationship("DocentesInDB", back_populates="grupos")"""
