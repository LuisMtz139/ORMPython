from sqlalchemy import Column, BigInteger, String, ForeignKey, Integer
from app.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship


from typing import Optional

class AsignaturasIn(BaseModel):  # Definición del modelo de entrada para crear una asignatura
    nombre: str
    creditos: int
    cuatrimestre: str
    plan_id: int

class AsignaturasOut(BaseModel):  # Definición del modelo de salida para obtener una asignatura
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
    user_id = Column(Integer, ForeignKey('user.id'))  # Agrega esta línea para definir la columna user_id
    
    # Definición de la relación con la tabla de usuarios
    user = relationship("UserInDB", back_populates="asignaturas")

   # plan_id = Column(BigInteger, ForeignKey('planes.id'))  # Clave foránea