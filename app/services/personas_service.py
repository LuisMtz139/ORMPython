from app.models.personas import PersonasIn, PersonasOut, PersonasInDB
from app.database import SessionLocal
from fastapi import HTTPException

class PersonasService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_persona(self, persona_data: PersonasIn):
        db_persona = PersonasInDB(**persona_data.dict()) 
        self.db.add(db_persona)
        self.db.commit()
        self.db.refresh(db_persona)
        return PersonasOut(**db_persona.__dict__)  

    async def get_persona(self, persona_id: int):
        persona = self.db.query(PersonasInDB).filter(PersonasInDB.id == persona_id).first()  
        if persona is None:
            raise HTTPException(status_code=404, detail="Persona not found")
        return PersonasOut(**persona.__dict__) 
    
    async def delete_persona(self, persona_id: int):
        persona = self.db.query(PersonasInDB).filter(PersonasInDB.id == persona_id).first()
        if persona is None:
            raise HTTPException(status_code=404, detail="Persona not found")
        self.db.delete(persona)
        self.db.commit()
        return PersonasOut(**persona.__dict__)

    async def update_persona(self, persona_id: int, persona_data: PersonasIn):
        persona = self.db.query(PersonasInDB).filter(PersonasInDB.id == persona_id).first()
        if persona is None:
            raise HTTPException(status_code=404, detail="Persona not found")
        for var, value in persona_data:
            setattr(persona, var, value)
        self.db.commit()
        self.db.refresh(persona)
        return PersonasOut(**persona.__dict__)
