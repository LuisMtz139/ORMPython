import random
from sqlalchemy import func  # Agrega esta línea para importar func

from app.database import SessionLocal
from app.models.periodos import PeriodosInDB
from app.models.cat_periodos import Cat_periodosInDB
from faker import Faker


def seed_periodos(num_periodos):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_periodos):
            cat_periodo = session.query(Cat_periodosInDB).order_by(func.random()).first()  # Usa func.random()

            periodo = PeriodosInDB(
                cat_periodo_id=cat_periodo.id,
                anio=random.randint(2000, 2021),
            )
            session.add(periodo)
        session.commit()
    finally:
        session.close()