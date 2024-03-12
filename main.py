from fastapi import FastAPI
from app.controllers import direccion_controller, user_controller , cat_periodos_controller, direccion_controller, docente_controller
from app.controllers import historial_status_estudiante_controller, asignaturas_controller,estatus_cardex_controller
from app.database import Base, engine  

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/people", tags=["people"])
app.include_router(direccion_controller.router, prefix="/direcciones", tags=["direcciones"])
app.include_router(cat_periodos_controller.router, prefix="/cat_periodos", tags=["cat_periodos"])
app.include_router(docente_controller.router, prefix="/docentes", tags=["docentes"])
app.include_router(historial_status_estudiante_controller.router, prefix="/historial_estatus_estudiantes", tags=["historial_estatus_estudiantes"])
app.include_router(asignaturas_controller.router, prefix="/asignaturas", tags=["asignaturas"])
app.include_router(estatus_cardex_controller.router, prefix="/estatus_cardex", tags=["estatus_cardex"])