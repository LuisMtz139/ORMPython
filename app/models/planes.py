from sqlalchemy import Column, BigInteger, String, Integer
from app.database import Base
from pydantic import BaseModel

class PlanesIn(BaseModel):
    nombre: str
    creditos: int

class PlanesOut(BaseModel):
    id: int
    nombre: str
    creditos: int

class PlanesDelete(BaseModel):
    id: int
    
class PlanesUpdate(BaseModel):
    id: int
    nombre: str
    creditos: int

class PlanesInDB(Base):
    __tablename__ = "planes"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    creditos = Column(Integer, nullable=False)
