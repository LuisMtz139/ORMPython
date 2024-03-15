from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel
from typing import Optional

class DireccionIn(BaseModel):  # Modelo para crear
    codigo_postal: str
    ciudad: str
    colonia: str
    numero_interior: str
    numero_exterior: str
    calle_1: str
    calle_2: str
    persona_id: int
    referencias_direccion: str
    

class DireccionOut(BaseModel):  # Modelo para obtener
    id: int
    codigo_postal: str
    ciudad: str
    colonia: str
    numero_interior: str
    numero_exterior: str
    calle_1: str
    calle_2: str
    persona_id: int
    referencias_direccion: str

class DireccionInDB(Base):  # Modelo de base de datos
    __tablename__ = "direcciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_postal = Column(String(10), index=True)
    ciudad = Column(String(50), index=True)
    colonia = Column(String(50), index=True)
    numero_interior = Column(String(10), index=True)
    numero_exterior = Column(String(10), index=True)
    calle_1 = Column(String(50), index=True)
    calle_2 = Column(String(50), index=True)
    persona_id = Column(Integer, ForeignKey('personas.id'))  # Clave foránea a la tabla de personas
    referencias_direccion = Column(String(255))

    persona = relationship("PersonasInDB", back_populates="direcciones")  # Relación inversa con personas
