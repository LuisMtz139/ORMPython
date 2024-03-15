from faker import Faker
from app.database import SessionLocal
from app.models.personas import PersonasInDB

def seed_personas(num_personas):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_personas):
            # Genera datos falsos para la persona
            persona_data = {
                "nombre": fake.first_name(),
                "apellido_paterno": fake.last_name(),
                "telefono": fake.phone_number(),
                "curp": fake.uuid4()[:18]  # Genera un CURP falso
            }
            # Crea una instancia del modelo PersonasInDB con los datos generados
            persona = PersonasInDB(**persona_data)
            session.add(persona)
        session.commit()
    finally:
        session.close()
