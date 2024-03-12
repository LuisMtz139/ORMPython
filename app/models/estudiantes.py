from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel
from typing import Optional 

class EstudiantesIn(BaseModel):
    matricula: str
    persona_id: int
    estatus_actual_id: int
    periodo_id: int
    tutor_id: Optional[int] = None

class EstudiantesOut(BaseModel):
    id: int
    matricula: str
    persona_id: int
    estatus_actual_id: int
    periodo_id: int
    tutor_id: Optional[int] = None

class EstudiantesDelete(BaseModel):
    id: int
    
class EstudiantesUpdate(BaseModel):
    id: int
    matricula: str
    persona_id: int
    estatus_actual_id: int
    periodo_id: int
    tutor_id: Optional[int] = None

class EstudiantesInDB(Base):
    __tablename__ = "estudiantes"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    matricula = Column(String(20), nullable=False, unique=True)
    persona_id = Column(BigInteger, ForeignKey("personas.id"), nullable=False)
    estatus_actual_id = Column(BigInteger, ForeignKey("estatus_estudiantes.id"), nullable=False)
    periodo_id = Column(BigInteger, ForeignKey("periodos.id"), nullable=False)
    tutor_id = Column(BigInteger, ForeignKey("docentes.id"), nullable=True)

    # Relaciones
    persona = relationship("PersonasInDB", back_populates="estudiantes")
    estatus_actual = relationship("EstatusEstudiantesInDB", back_populates="estudiantes")
    periodo = relationship("PeriodosInDB", back_populates="estudiantes")
    tutor = relationship("DocentesInDB", back_populates="estudiantes")