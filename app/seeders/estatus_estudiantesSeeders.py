from app.database import SessionLocal
from app.models.estatus_estudiantes import EstatusEstudiantesInDB
from faker import Faker
import random

fake = Faker()

def seed_estatus_estudiantes(num_estatus):
    session = SessionLocal()

    try:
        estatus_list = ["INSCRITO", "BAJA_DEFINITIVA", "BAJA_ACADEMICA", "TITULADO"]
        for i in range(num_estatus):
            estatus_data = {"estatus": random.choice(estatus_list) + "_" + str(i)}
            estatus = EstatusEstudiantesInDB(**estatus_data)
            session.add(estatus)
        session.commit()
    finally:
        session.close()