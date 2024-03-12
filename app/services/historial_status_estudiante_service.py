from app.models.historial_status_estudiante import Historial_status_estudianteIn, Historial_status_estudianteOut, Historial_status_estudianteInDB
from app.database import SessionLocal
from fastapi import HTTPException


class Historial_status_estudianteService:
    def __init__(self):
        self.db = SessionLocal()
        
        
    async def create_historial_status_estudiante(self, historial_status_estudiante_data: Historial_status_estudianteIn):
        db_historial_status_estudiante = Historial_status_estudianteInDB(**historial_status_estudiante_data.dict()) 
        self.db.add(db_historial_status_estudiante)
        self.db.commit()
        self.db.refresh(db_historial_status_estudiante)
        return Historial_status_estudianteOut(**db_historial_status_estudiante.__dict__)
    
    async def get_historial_status_estudiante(self, historial_status_estudiante_id: int):
        historial_status_estudiante = self.db.query(Historial_status_estudianteInDB).filter(Historial_status_estudianteInDB.id == historial_status_estudiante_id).first()
        if historial_status_estudiante is None:
            raise HTTPException(status_code=404, detail="Historial_status_estudiante not found")
        return Historial_status_estudianteOut(**historial_status_estudiante.__dict__)
    
    async def delete_historial_status_estudiante(self, historial_status_estudiante_id: int):
        historial_status_estudiante = self.db.query(Historial_status_estudianteInDB).filter(Historial_status_estudianteInDB.id == historial_status_estudiante_id).first()
        if historial_status_estudiante is None:
            raise HTTPException(status_code=404, detail="Historial_status_estudiante not found")
        self.db.delete(historial_status_estudiante)
        self.db.commit()
        return Historial_status_estudianteOut(**historial_status_estudiante.__dict__)
    
    async def update_historial_status_estudiante(self, historial_status_estudiante_id: int, historial_status_estudiante_data: Historial_status_estudianteIn):
        historial_status_estudiante = self.db.query(Historial_status_estudianteInDB).filter(Historial_status_estudianteInDB.id == historial_status_estudiante_id).first()
        if historial_status_estudiante is None:
            raise HTTPException(status_code=404, detail="Historial_status_estudiante not found")
        for var, value in historial_status_estudiante_data:
            setattr(historial_status_estudiante, var, value)
        self.db.commit()
        self.db.refresh(historial_status_estudiante)
        return Historial_status_estudianteOut(**historial_status_estudiante.__dict__)
    