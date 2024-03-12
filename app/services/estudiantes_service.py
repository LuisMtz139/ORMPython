from app.models.estudiantes import EstudiantesIn, EstudiantesOut, EstudiantesInDB
from app.database import SessionLocal
from fastapi import HTTPException

class EstudiantesService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_estudiante(self, estudiante_data: EstudiantesIn):
        db_estudiante = EstudiantesInDB(**estudiante_data.dict()) 
        self.db.add(db_estudiante)
        self.db.commit()
        self.db.refresh(db_estudiante)
        return EstudiantesOut(**db_estudiante.__dict__)  

    async def get_estudiante(self, estudiante_id: int):
        estudiante = self.db.query(EstudiantesInDB).filter(EstudiantesInDB.id == estudiante_id).first()  
        if estudiante is None:
            raise HTTPException(status_code=404, detail="Estudiante not found")
        return EstudiantesOut(**estudiante.__dict__) 
    
    async def delete_estudiante(self, estudiante_id: int):
        estudiante = self.db.query(EstudiantesInDB).filter(EstudiantesInDB.id == estudiante_id).first()
        if estudiante is None:
            raise HTTPException(status_code=404, detail="Estudiante not found")
        self.db.delete(estudiante)
        self.db.commit()
        return EstudiantesOut(**estudiante.__dict__)

    async def update_estudiante(self, estudiante_id: int, estudiante_data: EstudiantesIn):
        estudiante = self.db.query(EstudiantesInDB).filter(EstudiantesInDB.id == estudiante_id).first()
        if estudiante is None:
            raise HTTPException(status_code=404, detail="Estudiante not found")
        for var, value in estudiante_data:
            setattr(estudiante, var, value)
        self.db.commit()
        self.db.refresh(estudiante)
        return EstudiantesOut(**estudiante.__dict__)
