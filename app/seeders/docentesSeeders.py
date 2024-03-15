import random
from sqlalchemy import func  # Agrega esta línea para importar func
from app.database import SessionLocal

from app.models.docentes import DocentesInDB
from app.models.personas import PersonasInDB
from faker import Faker

def seed_docentes(num_docentes):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_docentes):
            persona = session.query(PersonasInDB).order_by(func.random()).first()  # Usa func.random()

            docente = DocentesInDB(
                persona_id=persona.id,
            )
            session.add(docente)
        session.commit()
    finally:
        session.close()