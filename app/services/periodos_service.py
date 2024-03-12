from app.models.periodos import PeriodosIn, PeriodosOut, PeriodosInDB
from app.database import SessionLocal
from fastapi import HTTPException

class PeriodosService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_periodo(self, periodo_data: PeriodosIn):
        db_periodo = PeriodosInDB(**periodo_data.dict()) 
        self.db.add(db_periodo)
        self.db.commit()
        self.db.refresh(db_periodo)
        return PeriodosOut(**db_periodo.__dict__)  

    async def get_periodo(self, periodo_id: int):
        periodo = self.db.query(PeriodosInDB).filter(PeriodosInDB.id == periodo_id).first()  
        if periodo is None:
            raise HTTPException(status_code=404, detail="Periodo not found")
        return PeriodosOut(**periodo.__dict__) 
    
    async def delete_periodo(self, periodo_id: int):
        periodo = self.db.query(PeriodosInDB).filter(PeriodosInDB.id == periodo_id).first()
        if periodo is None:
            raise HTTPException(status_code=404, detail="Periodo not found")
        self.db.delete(periodo)
        self.db.commit()
        return PeriodosOut(**periodo.__dict__)

    async def update_periodo(self, periodo_id: int, periodo_data: PeriodosIn):
        periodo = self.db.query(PeriodosInDB).filter(PeriodosInDB.id == periodo_id).first()
        if periodo is None:
            raise HTTPException(status_code=404, detail="Periodo not found")
        for var, value in periodo_data:
            setattr(periodo, var, value)
        self.db.commit()
        self.db.refresh(periodo)
        return PeriodosOut(**periodo.__dict__)
