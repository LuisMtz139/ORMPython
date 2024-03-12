from app.models.cat_periodos import Cat_periodosIn, Cat_periodosOut, Cat_periodosInDB
from app.database import SessionLocal
from fastapi import HTTPException


class Cat_periodosService:
    def __init__(self):
        self.db = SessionLocal()
        
    async def create_cat_periodos(self, cat_periodos_data: Cat_periodosIn):
        db_cat_periodos = Cat_periodosInDB(**cat_periodos_data.dict()) 
        self.db.add(db_cat_periodos)
        self.db.commit()
        self.db.refresh(db_cat_periodos)
        return Cat_periodosOut(**db_cat_periodos.__dict__)
    
    async def get_cat_periodos(self, cat_periodos_id: int):
        cat_periodos = self.db.query(Cat_periodosInDB).filter(Cat_periodosInDB.id == cat_periodos_id).first()
        if cat_periodos is None:
            raise HTTPException(status_code=404, detail="Cat_periodos not found")
        return Cat_periodosOut(**cat_periodos.__dict__)
    
    async def delete_cat_periodos(self, cat_periodos_id: int):
        cat_periodos = self.db.query(Cat_periodosInDB).filter(Cat_periodosInDB.id == cat_periodos_id).first()
        if cat_periodos is None:
            raise HTTPException(status_code=404, detail="Cat_periodos not found")
        self.db.delete(cat_periodos)
        self.db.commit()
        return Cat_periodosOut(**cat_periodos.__dict__)
    
    async def update_cat_periodos(self, cat_periodos_id: int, cat_periodos_data: Cat_periodosIn):
        cat_periodos = self.db.query(Cat_periodosInDB).filter(Cat_periodosInDB.id == cat_periodos_id).first()
        if cat_periodos is None:
            raise HTTPException(status_code=404, detail="Cat_periodos not found")
        for var, value in cat_periodos_data:
            setattr(cat_periodos, var, value)
        self.db.commit()
        self.db.refresh(cat_periodos)
        return Cat_periodosOut(**cat_periodos.__dict__)