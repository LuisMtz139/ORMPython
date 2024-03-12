from fastapi import FastAPI
from app.controllers import user_controller
from app.controllers import personas_controller
from app.controllers import estatus_estudiantes_controller
from app.controllers import periodos_controller
from app.controllers import estudiantes_controller
from app.controllers import planes_controller
from app.controllers import grupos_controller
from app.controllers import calificaciones_controller






from app.database import Base, engine  


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/people", tags=["people"])
app.include_router(personas_controller.router, prefix="/personas", tags=["personas"])
app.include_router(estatus_estudiantes_controller.router, prefix="/estatus_estudiante", tags=["estatus_estudiante"])
app.include_router(periodos_controller.router, prefix="/periodos", tags=["periodos"])
app.include_router(estudiantes_controller.router, prefix="/estudiantes", tags=["estudiantes"])


