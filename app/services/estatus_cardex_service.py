from app.models.estatus_cardex import Estatus_cardexIn, Estatus_cardexOut, Estatus_cardexInDB
from app.database import SessionLocal
from fastapi import HTTPException

class Estatus_cardexService:
    def __init__(self):
        self.db = SessionLocal()
        

    async def create_estatus_cardex(self, estatus_cardex_data: Estatus_cardexIn):
        db_estatus_cardex = Estatus_cardexInDB(**estatus_cardex_data.dict()) 
        self.db.add(db_estatus_cardex)
        self.db.commit()
        self.db.refresh(db_estatus_cardex)
        return Estatus_cardexOut(**db_estatus_cardex.__dict__)
    
    async def get_estatus_cardex(self, estatus_cardex_id: int):
        estatus_cardex = self.db.query(Estatus_cardexInDB).filter(Estatus_cardexInDB.id == estatus_cardex_id).first()
        if estatus_cardex is None:
            raise HTTPException(status_code=404, detail="Estatus_cardex not found")
        return Estatus_cardexOut(**estatus_cardex.__dict__)
    
    async def delete_estatus_cardex(self, estatus_cardex_id: int):
        estatus_cardex = self.db.query(Estatus_cardexInDB).filter(Estatus_cardexInDB.id == estatus_cardex_id).first()
        if estatus_cardex is None:
            raise HTTPException(status_code=404, detail="Estatus_cardex not found")
        self.db.delete(estatus_cardex)
        self.db.commit()
        return Estatus_cardexOut(**estatus_cardex.__dict__)
    
    async def update_estatus_cardex(self, estatus_cardex_id: int, estatus_cardex_data: Estatus_cardexIn):
        estatus_cardex = self.db.query(Estatus_cardexInDB).filter(Estatus_cardexInDB.id == estatus_cardex_id).first()
        if estatus_cardex is None:
            raise HTTPException(status_code=404, detail="Estatus_cardex not found")
        for var, value in estatus_cardex_data:
            setattr(estatus_cardex, var, value)
        self.db.commit()
        self.db.refresh(estatus_cardex)
        return Estatus_cardexOut(**estatus_cardex.__dict__)