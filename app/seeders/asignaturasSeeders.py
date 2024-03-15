from sqlalchemy import func  # Agrega esta línea para importar func

from faker import Faker
from app.database import SessionLocal
from app.models.user import UserInDB
from app.models.asignaturas import AsignaturasInDB

def seed_asignaturas(num_asignaturas):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_asignaturas):
            user = session.query(UserInDB).order_by(func.random()).first()  # Usa func.random()
            
            asignatura = AsignaturasInDB(
                nombre=fake.word(),
                creditos=fake.random_int(min=1, max=6),
                cuatrimestre=fake.word(),
                user_id=user.id
            )
            session.add(asignatura)
        session.commit()
    finally:
        session.close()
