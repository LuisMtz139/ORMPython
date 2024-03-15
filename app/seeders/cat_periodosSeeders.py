from faker import Faker
from app.database import SessionLocal
from app.models.cat_periodos import Cat_periodosInDB
from app.models.cat_periodos import Cat_periodosInDB

def seed_cat_periodos(num_people):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_people):
            cat_periodos = Cat_periodosInDB(
                periodo=fake.word(),
            )
            session.add(cat_periodos)
        session.commit()
    finally:
        session.close()
