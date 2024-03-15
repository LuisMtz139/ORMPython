from faker import Faker
from app.database import SessionLocal
from app.models.historial_status_estudiante import Historial_status_estudianteInDB


def seed_historial_status_estudiante(num_historial_status_estudiante):
    fake = Faker()
    session = SessionLocal()

    try:
        for _ in range(num_historial_status_estudiante):
            historial_status_estudiante = Historial_status_estudianteInDB(
                estatus_estudiante_id=fake.random_int(min=1, max=num_historial_status_estudiante),  # Adjust the range as needed
            )
            session.add(historial_status_estudiante)
        session.commit()
    finally:
        session.close()