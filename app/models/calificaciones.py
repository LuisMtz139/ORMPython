from sqlalchemy import Column, BigInteger, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel

class CalificacionesIn(BaseModel):
    ordinario_1: float = None
    ordinario_2: float = None
    ordinario_3: float = None
    recuperacion_1: float = None
    recuperacion_2: float = None
    recuperacion_3: float = None
    extra: float
    final: float
    grupo_id: int
    estudiante_id: int
    estatus_cardex_id: int = None

class CalificacionesOut(BaseModel):
    id: int
    ordinario_1: float
    ordinario_2: float
    ordinario_3: float
    recuperacion_1: float
    recuperacion_2: float
    recuperacion_3: float
    extra: float
    final: float
    grupo_id: int
    estudiante_id: int
    estatus_cardex_id: int

class CalificacionesDelete(BaseModel):
    id: int
    
class CalificacionesUpdate(BaseModel):
    id: int
    ordinario_1: float
    ordinario_2: float
    ordinario_3: float
    recuperacion_1: float
    recuperacion_2: float
    recuperacion_3: float
    extra: float
    final: float
    grupo_id: int
    estudiante_id: int
    estatus_cardex_id: int

class CalificacionesInDB(Base):
    __tablename__ = "calificaciones"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    ordinario_1 = Column(Float)
    ordinario_2 = Column(Float)
    ordinario_3 = Column(Float)
    recuperacion_1 = Column(Float)
    recuperacion_2 = Column(Float)
    recuperacion_3 = Column(Float)
    extra = Column(Float)
    final = Column(Float)
   # grupo_id = Column(BigInteger, ForeignKey("grupos.id"))
   # estudiante_id = Column(BigInteger, ForeignKey("estudiantes.id"))
  #  estatus_cardex_id = Column(BigInteger, ForeignKey("estatus_cardex.id"), nullable=True)

    # Relaciones
   # grupo = relationship("GruposInDB", back_populates="calificaciones")
   # estudiante = relationship("EstudiantesInDB", back_populates="calificaciones")
   # estatus_cardex = relationship("EstatusCardexInDB", back_populates="calificaciones")