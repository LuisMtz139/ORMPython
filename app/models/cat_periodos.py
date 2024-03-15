from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship


from typing import Optional

class Cat_periodosIn(BaseModel):#crear
    periodo: str



class Cat_periodosOut(BaseModel):#obtener
    id: int
    periodo: str
    
    

class Cat_periodosInDB(Base):
    __tablename__ = "cat_periodos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    periodo = Column(String(50), index=True)
    
    
    periodos = relationship("PeriodosInDB", back_populates="cat_periodos")  # Relación con direcciones

