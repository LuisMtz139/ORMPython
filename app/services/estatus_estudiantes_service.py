from app.models.estatus_estudiantes import EstatusEstudiantesIn, EstatusEstudiantesOut, EstatusEstudiantesInDB
from app.database import SessionLocal
from fastapi import HTTPException

class EstatusEstudiantesService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_estatus_estudiante(self, estatus_data: EstatusEstudiantesIn):
        db_estatus = EstatusEstudiantesInDB(**estatus_data.dict()) 
        self.db.add(db_estatus)
        self.db.commit()
        self.db.refresh(db_estatus)
        return EstatusEstudiantesOut(**db_estatus.__dict__)  

    async def get_estatus_estudiante(self, estatus_id: int):
        estatus = self.db.query(EstatusEstudiantesInDB).filter(EstatusEstudiantesInDB.id == estatus_id).first()  
        if estatus is None:
            raise HTTPException(status_code=404, detail="Estatus estudiante not found")
        return EstatusEstudiantesOut(**estatus.__dict__) 
    
    async def delete_estatus_estudiante(self, estatus_id: int):
        estatus = self.db.query(EstatusEstudiantesInDB).filter(EstatusEstudiantesInDB.id == estatus_id).first()
        if estatus is None:
            raise HTTPException(status_code=404, detail="Estatus estudiante not found")
        self.db.delete(estatus)
        self.db.commit()
        return EstatusEstudiantesOut(**estatus.__dict__)

    async def update_estatus_estudiante(self, estatus_id: int, estatus_data: EstatusEstudiantesIn):
        estatus = self.db.query(EstatusEstudiantesInDB).filter(EstatusEstudiantesInDB.id == estatus_id).first()
        if estatus is None:
            raise HTTPException(status_code=404, detail="Estatus estudiante not found")
        for var, value in estatus_data:
            setattr(estatus, var, value)
        self.db.commit()
        self.db.refresh(estatus)
        return EstatusEstudiantesOut(**estatus.__dict__)
