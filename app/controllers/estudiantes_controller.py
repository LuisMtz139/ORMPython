from fastapi import APIRouter, Depends
from app.services.estudiantes_service import EstudiantesService
from app.models.estudiantes import EstudiantesIn, EstudiantesOut, EstudiantesDelete, EstudiantesUpdate

router = APIRouter()
estudiantes_service = EstudiantesService()

@router.post("/", response_model=EstudiantesOut)
async def create_estudiante(estudiante_data: EstudiantesIn):
    return await estudiantes_service.create_estudiante(estudiante_data)

@router.get("/{estudiante_id}", response_model=EstudiantesOut)
async def get_estudiante(estudiante_id: int):
    return await estudiantes_service.get_estudiante(estudiante_id)

@router.delete("/{estudiante_id}", response_model=EstudiantesOut)
async def delete_estudiante(estudiante_id: int):
    return await estudiantes_service.delete_estudiante(estudiante_id)

@router.put("/{estudiante_id}", response_model=EstudiantesOut)
async def update_estudiante(estudiante_id: int, estudiante_data: EstudiantesIn):
    return await estudiantes_service.update_estudiante(estudiante_id, estudiante_data)
