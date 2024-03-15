from faker import Faker
from app.database import SessionLocal
from app.models.planes import PlanesInDB




def seed_planes(num_planes):
    fake = Faker()
    db = SessionLocal()
    for _ in range(num_planes):
        plan = PlanesInDB(
            nombre=fake.word(),
            creditos=fake.random_int(min=1, max=num_planes)
        )
        db.add(plan)
    db.commit()
    db.close()