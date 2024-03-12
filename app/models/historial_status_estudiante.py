
from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

from typing import Optional


class Historial_status_estudianteIn(BaseModel):#crear
    estudiante_id: int
    estatus_estudiante_id: int

class Historial_status_estudianteOut(BaseModel):#obtener
    id: int
    estudiante_id: int
    estatus_estudiante_id: int
    
    

class Historial_status_estudianteInDB(Base):
    __tablename__ = "historial_estatus_estudiantes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    estudiante_id = Column(Integer, index=True)
    estatus_estudiante_id = Column(Integer, index=True)