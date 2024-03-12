from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel

from typing import Optional

class PersonasIn(BaseModel):#crear
    nombre: str
    apellido_paterno: str
    telefono: str
    curp: Optional[str] = None

class PersonasOut(BaseModel):#obtener
    id: int
    nombre: str
    apellido_paterno: str
    telefono: str
    curp: Optional[str] = None

class PersonasDelete(BaseModel):
    id: int
    
class PersonasUpdate(BaseModel):
    id: int
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    telefono: Optional[str] = None
    curp: Optional[str] = None

class PersonasInDB(Base):
    __tablename__ = "personas"  # Nombre de la tabla cambiado

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True) 
    apellido_paterno = Column(String(50), index=True)  
    telefono = Column(String(50), nullable=True)  
    curp = Column(String(18), nullable=True)  
    persona_id = Column(BigInteger, ForeignKey('personas.id'))  # Clave foránea