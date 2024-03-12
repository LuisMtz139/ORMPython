from app.models.calificaciones import CalificacionesIn, CalificacionesOut, CalificacionesDelete, CalificacionesUpdate, CalificacionesInDB
from app.database import SessionLocal
from fastapi import HTTPException

class CalificacionesService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_calificaciones(self, calificaciones_data: CalificacionesIn):
        db_calificaciones = CalificacionesInDB(**calificaciones_data.dict()) 
        self.db.add(db_calificaciones)
        self.db.commit()
        self.db.refresh(db_calificaciones)
        return CalificacionesOut(**db_calificaciones.__dict__)  

    async def get_calificaciones(self, calificaciones_id: int):
        calificaciones = self.db.query(CalificacionesInDB).filter(CalificacionesInDB.id == calificaciones_id).first()  
        if calificaciones is None:
            raise HTTPException(status_code=404, detail="Calificaciones not found")
        return CalificacionesOut(**calificaciones.__dict__) 
    
    async def delete_calificaciones(self, calificaciones_id: int):
        calificaciones = self.db.query(CalificacionesInDB).filter(CalificacionesInDB.id == calificaciones_id).first()
        if calificaciones is None:
            raise HTTPException(status_code=404, detail="Calificaciones not found")
        self.db.delete(calificaciones)
        self.db.commit()
        return CalificacionesOut(**calificaciones.__dict__)

    async def update_calificaciones(self, calificaciones_id: int, calificaciones_data: CalificacionesUpdate):
        calificaciones = self.db.query(CalificacionesInDB).filter(CalificacionesInDB.id == calificaciones_id).first()
        if calificaciones is None:
            raise HTTPException(status_code=404, detail="Calificaciones not found")
        for var, value in calificaciones_data:
            setattr(calificaciones, var, value)
        self.db.commit()
        self.db.refresh(calificaciones)
        return CalificacionesOut(**calificaciones.__dict__)
