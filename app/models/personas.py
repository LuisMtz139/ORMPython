from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel
from typing import Optional

class PersonasIn(BaseModel):  # Modelo para crear
    nombre: str
    apellido_paterno: str
    telefono: str
    curp: Optional[str] = None

class PersonasOut(BaseModel):  # Modelo para obtener
    id: int
    nombre: str
    apellido_paterno: str
    telefono: str
    curp: Optional[str] = None

class PersonasDelete(BaseModel):  # Modelo para eliminar
    id: int
    
class PersonasUpdate(BaseModel):  # Modelo para actualizar
    id: int
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    telefono: Optional[str] = None
    curp: Optional[str] = None

class PersonasInDB(Base):  # Modelo de base de datos
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True) 
    apellido_paterno = Column(String(50), index=True)  
    telefono = Column(String(50), nullable=True)  
    curp = Column(String(18), nullable=True)

    direcciones = relationship("DireccionInDB", back_populates="persona")  # Relación con direcciones

    docentes = relationship("DocentesInDB", back_populates="persona")

