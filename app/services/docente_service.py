from app.models.docentes import DocentesIn,DocentesInDB,DocentesOut
from app.database import SessionLocal
from fastapi import HTTPException



class DocenteService:
    def __init__(self):
        self.db = SessionLocal()
        
    async def create_docente(self, docente_data: DocentesIn):
        db_docente = DocentesInDB(**docente_data.dict()) 
        self.db.add(db_docente)
        self.db.commit()
        self.db.refresh(db_docente)
        return DocentesOut(**db_docente.__dict__)
    
    async def get_docente(self, docente_id: int):
        docente = self.db.query(DocentesInDB).filter(DocentesInDB.id == docente_id).first()
        if docente is None:
            raise HTTPException(status_code=404, detail="Docente not found")
        return DocentesOut(**docente.__dict__)
    
    async def delete_docente(self, docente_id: int):
        docente = self.db.query(DocentesInDB).filter(DocentesInDB.id == docente_id).first()
        if docente is None:
            raise HTTPException(status_code=404, detail="Docente not found")
        self.db.delete(docente)
        self.db.commit()
        return DocentesOut(**docente.__dict__)

    async def update_docente(self, docente_id: int, docente_data: DocentesIn):
        docente = self.db.query(DocentesInDB).filter(DocentesInDB.id == docente_id).first()
        if docente is None:
            raise HTTPException(status_code=404, detail="Docente not found")
        for var, value in docente_data:
            setattr(docente, var, value)
        self.db.commit()
        self.db.refresh(docente)
        return DocentesOut(**docente.__dict__)
