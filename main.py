from fastapi import FastAPI

from app.controllers import direccion_controller, user_controller , cat_periodos_controller, direccion_controller, docente_controller
from app.controllers import historial_status_estudiante_controller, asignaturas_controller,estatus_cardex_controller
from app.controllers import user_controller
from app.controllers import personas_controller
from app.controllers import estatus_estudiantes_controller
from app.controllers import periodos_controller
from app.controllers import estudiantes_controller
from app.controllers import planes_controller
from app.controllers import grupos_controller
from app.controllers import calificaciones_controller
from app.controllers import planes_controller


from app.seeders import userSeeders
from app.seeders import asignaturasSeeders
from app.seeders import direccionesSeeders
from app.seeders import personaSeeders
from app.database import Base, engine  
from app.seeders import estatus_estudiantesSeeders
from app.seeders import cat_periodosSeeders
from app.seeders import periodosSeeders
from app.seeders import docentesSeeders
from app.seeders import estatus_cardexSeeders
from app.seeders import historial_estatus_estudiantesSeeders
from app.seeders import planesSeeders
app = FastAPI()

Base.metadata.create_all(bind=engine)

personaSeeders.seed_personas(100)
direccionesSeeders.seed_direcciones(100)
estatus_estudiantesSeeders.seed_estatus_estudiantes(100)
cat_periodosSeeders.seed_cat_periodos(100)
periodosSeeders.seed_periodos(100)
docentesSeeders.seed_docentes(100)
#estudiantes
historial_estatus_estudiantesSeeders.seed_historial_status_estudiante(100)
planesSeeders.seed_planes(100)
asignaturasSeeders.seed_asignaturas(100)
#grupos
estatus_cardexSeeders.seed_estatus_cardex(100)
#calificaciones
userSeeders.seed_people(100) ##se hace el llamo a seeders user 


app.include_router(personas_controller.router, prefix="/personas", tags=["personas"])
app.include_router(direccion_controller.router, prefix="/direcciones", tags=["direcciones"])
app.include_router(estatus_estudiantes_controller.router, prefix="/estatus_estudiante", tags=["estatus_estudiante"])
app.include_router(cat_periodos_controller.router, prefix="/cat_periodos", tags=["cat_periodos"])
app.include_router(periodos_controller.router, prefix="/periodos", tags=["periodos"]) #catperiodos
app.include_router(estatus_estudiantes_controller.router, prefix="/estatus_estudiante", tags=["estatus_estudiante"])
app.include_router(cat_periodos_controller.router, prefix="/cat_periodos", tags=["cat_periodos"])
app.include_router(periodos_controller.router, prefix="/periodos", tags=["periodos"]) #catperiodos
app.include_router(docente_controller.router, prefix="/docentes", tags=["docentes"])
app.include_router(estatus_cardex_controller.router, prefix="/estatus_cardex", tags=["estatus_cardex"])
app.include_router(planes_controller.router, prefix="/planes", tags=["planes"])


app.include_router(user_controller.router, prefix="/people", tags=["people"])

app.include_router(direccion_controller.router, prefix="/direcciones", tags=["direcciones"])
app.include_router(historial_status_estudiante_controller.router, prefix="/historial_estatus_estudiantes", tags=["historial_estatus_estudiantes"])
app.include_router(asignaturas_controller.router, prefix="/asignaturas", tags=["asignaturas"])

app.include_router(personas_controller.router, prefix="/personas", tags=["personas"])
app.include_router(periodos_controller.router, prefix="/periodos", tags=["periodos"])
app.include_router(estudiantes_controller.router, prefix="/estudiantes", tags=["estudiantes"])