from app.models.direccion import DireccionIn, DireccionOut, DireccionInDB
from app.database import SessionLocal
from fastapi import HTTPException

class DireccionService:
    def __init__(self):
        self.db = SessionLocal()
        
    async def create_direccion(self, direccion_data: DireccionIn):
        db_direccion = DireccionInDB(**direccion_data.dict()) 
        self.db.add(db_direccion)
        self.db.commit()
        self.db.refresh(db_direccion)
        return DireccionOut(**db_direccion.__dict__)
    
    async def get_direccion(self, direccion_id: int):
        direccion = self.db.query(DireccionInDB).filter(DireccionInDB.id == direccion_id).first()
        if direccion is None:
            raise HTTPException(status_code=404, detail="Direccion not found")
        return DireccionOut(**direccion.__dict__)  
    
    async def delete_direccion(self, direccion_id: int):
        direccion = self.db.query(DireccionInDB).filter(DireccionInDB.id == direccion_id).first()
        if direccion is None:
            raise HTTPException(status_code=404, detail="Direccion not found")
        self.db.delete(direccion)
        self.db.commit()
        return DireccionOut(**direccion.__dict__)
    
    async def update_direccion(self, direccion_id: int, direccion_data: DireccionIn):
        direccion = self.db.query(DireccionInDB).filter(DireccionInDB.id == direccion_id).first()
        if direccion is None:
            raise HTTPException(status_code=404, detail="Direccion not found")
        for var, value in direccion_data:
            setattr(direccion, var, value)
        self.db.commit()
        self.db.refresh(direccion)
        return DireccionOut(**direccion.__dict__)