from sqlalchemy import Column, BigInteger, String, CheckConstraint
from app.database import Base
from pydantic import BaseModel

class EstatusEstudiantesIn(BaseModel):
    estatus: str

class EstatusEstudiantesOut(BaseModel):
    id: int
    estatus: str

class EstatusEstudiantesDelete(BaseModel):
    id: int
    
class EstatusEstudiantesUpdate(BaseModel):
    id: int
    estatus: str

class EstatusEstudiantesInDB(Base):
    __tablename__ = "estatus_estudiantes"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    estatus = Column(String(50), nullable=False, unique=True)

    __table_args__ = (
        CheckConstraint(
            'estatus IN ("INSCRITO", "BAJA_DEFINITIVA", "BAJA_ACADEMICA", "TITULADO")',
            name='estatus_check'
        ),
    )
