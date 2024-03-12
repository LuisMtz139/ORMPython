from app.models.planes import PlanesIn, PlanesOut, PlanesDelete, PlanesUpdate, PlanesInDB
from app.database import SessionLocal
from fastapi import HTTPException

class PlanesService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_planes(self, planes_data: PlanesIn):
        db_planes = PlanesInDB(**planes_data.dict()) 
        self.db.add(db_planes)
        self.db.commit()
        self.db.refresh(db_planes)
        return PlanesOut(**db_planes.__dict__)  

    async def get_planes(self, planes_id: int):
        planes = self.db.query(PlanesInDB).filter(PlanesInDB.id == planes_id).first()  
        if planes is None:
            raise HTTPException(status_code=404, detail="Planes not found")
        return PlanesOut(**planes.__dict__) 
    
    async def delete_planes(self, planes_id: int):
        planes = self.db.query(PlanesInDB).filter(PlanesInDB.id == planes_id).first()
        if planes is None:
            raise HTTPException(status_code=404, detail="Planes not found")
        self.db.delete(planes)
        self.db.commit()
        return PlanesOut(**planes.__dict__)

    async def update_planes(self, planes_id: int, planes_data: PlanesUpdate):
        planes = self.db.query(PlanesInDB).filter(PlanesInDB.id == planes_id).first()
        if planes is None:
            raise HTTPException(status_code=404, detail="Planes not found")
        for var, value in planes_data:
            setattr(planes, var, value)
        self.db.commit()
        self.db.refresh(planes)
        return PlanesOut(**planes.__dict__)
