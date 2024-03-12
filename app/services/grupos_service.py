from app.models.grupos import GruposIn, GruposOut, GruposDelete, GruposUpdate, GruposInDB
from app.database import SessionLocal
from fastapi import HTTPException

class GruposService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_grupos(self, grupos_data: GruposIn):
        db_grupos = GruposInDB(**grupos_data.dict()) 
        self.db.add(db_grupos)
        self.db.commit()
        self.db.refresh(db_grupos)
        return GruposOut(**db_grupos.__dict__)  

    async def get_grupos(self, grupos_id: int):
        grupos = self.db.query(GruposInDB).filter(GruposInDB.id == grupos_id).first()  
        if grupos is None:
            raise HTTPException(status_code=404, detail="Grupos not found")
        return GruposOut(**grupos.__dict__) 
    
    async def delete_grupos(self, grupos_id: int):
        grupos = self.db.query(GruposInDB).filter(GruposInDB.id == grupos_id).first()
        if grupos is None:
            raise HTTPException(status_code=404, detail="Grupos not found")
        self.db.delete(grupos)
        self.db.commit()
        return GruposOut(**grupos.__dict__)

    async def update_grupos(self, grupos_id: int, grupos_data: GruposUpdate):
        grupos = self.db.query(GruposInDB).filter(GruposInDB.id == grupos_id).first()
        if grupos is None:
            raise HTTPException(status_code=404, detail="Grupos not found")
        for var, value in grupos_data:
            setattr(grupos, var, value)
        self.db.commit()
        self.db.refresh(grupos)
        return GruposOut(**grupos.__dict__)
