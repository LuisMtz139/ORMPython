from faker import Faker
from app.database import SessionLocal
from app.models.estatus_cardex import Estatus_cardexInDB

def seed_estatus_cardex(num_estatus_cardex):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_estatus_cardex):
            estatus_cardex = Estatus_cardexInDB(
                estatus=fake.word(),
            )
            session.add(estatus_cardex)
        session.commit()
    finally:
        session.close()
