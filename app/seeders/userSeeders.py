from faker import Faker
from app.database import SessionLocal
from app.models.user import UserInDB

def seed_people(num_people):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_people):
            person = UserInDB(
                full_name=fake.name(),
                phone=fake.phone_number()[:20],
                password=fake.password(),
            )
            session.add(person)
        session.commit()
    finally:
        session.close()

  # Genera y guarda 100 personas en la base de datos
