import random
from sqlalchemy import func  # Agrega esta línea para importar func

from app.database import SessionLocal
from app.models.personas import PersonasInDB
from app.models.direccion import DireccionInDB
from faker import Faker
from app.models.personas import PersonasInDB


def seed_direcciones(num_direcciones):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_direcciones):
            persona = session.query(PersonasInDB).order_by(func.random()).first()  # Usa func.random()

            
            direccion = DireccionInDB(
                persona_id=persona.id,
                codigo_postal=fake.postcode(),
                ciudad=fake.city(),
                colonia=fake.street_name(),
                numero_interior=fake.building_number(),
                numero_exterior=fake.building_number(),
                calle_1=fake.street_name(),
                calle_2=fake.street_name(),
                referencias_direccion=fake.street_name(),
            )
            
            session.add(direccion)
        
        session.commit()
    
    finally:
        session.close()
