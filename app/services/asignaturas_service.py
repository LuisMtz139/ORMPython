from app.models.asignaturas import AsignaturasIn, AsignaturasOut, AsignaturasInDB
from app.database import SessionLocal
from fastapi import HTTPException

class AsignaturasService:
    def __init__(self):
        self.db = SessionLocal()
        
    async def create_asignatura(self, asignatura_data: AsignaturasIn):
        db_asignatura = AsignaturasInDB(**asignatura_data.dict()) 
        self.db.add(db_asignatura)
        self.db.commit()
        self.db.refresh(db_asignatura)
        return AsignaturasOut(**db_asignatura.__dict__)
    
    async def get_asignatura(self, asignatura_id: int):
        asignatura = self.db.query(AsignaturasInDB).filter(AsignaturasInDB.id == asignatura_id).first()
        if asignatura is None:
            raise HTTPException(status_code=404, detail="Asignatura not found")
        return AsignaturasOut(**asignatura.__dict__)
    
    async def delete_asignatura(self, asignatura_id: int):
        asignatura = self.db.query(AsignaturasInDB).filter(AsignaturasInDB.id == asignatura_id).first()
        if asignatura is None:
            raise HTTPException(status_code=404, detail="Asignatura not found")
        self.db.delete(asignatura)
        self.db.commit()
        return AsignaturasOut(**asignatura.__dict__)
    
    async def update_asignatura(self, asignatura_id: int, asignatura_data: AsignaturasIn):
        asignatura = self.db.query(AsignaturasInDB).filter(AsignaturasInDB.id == asignatura_id).first()
        if asignatura is None:
            raise HTTPException(status_code=404, detail="Asignatura not found")
        for var, value in asignatura_data:
            setattr(asignatura, var, value)
        self.db.commit()
        self.db.refresh(asignatura)
        return AsignaturasOut(**asignatura.__dict__)