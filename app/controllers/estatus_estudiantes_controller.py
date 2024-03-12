from fastapi import APIRouter, Depends
from app.services.estatus_estudiantes_service import EstatusEstudiantesService
from app.models.estatus_estudiantes import EstatusEstudiantesIn, EstatusEstudiantesOut, EstatusEstudiantesDelete, EstatusEstudiantesUpdate

router = APIRouter()
estatus_estudiantes_service = EstatusEstudiantesService()

@router.post("/", response_model=EstatusEstudiantesOut)
async def create_estatus_estudiante(estatus_data: EstatusEstudiantesIn):
    return await estatus_estudiantes_service.create_estatus_estudiante(estatus_data)

@router.get("/{estatus_id}", response_model=EstatusEstudiantesOut)
async def get_estatus_estudiante(estatus_id: int):
    return await estatus_estudiantes_service.get_estatus_estudiante(estatus_id)

@router.delete("/{estatus_id}", response_model=EstatusEstudiantesOut)
async def delete_estatus_estudiante(estatus_id: int):
    return await estatus_estudiantes_service.delete_estatus_estudiante(estatus_id)

@router.put("/{estatus_id}", response_model=EstatusEstudiantesOut)
async def update_estatus_estudiante(estatus_id: int, estatus_data: EstatusEstudiantesIn):
    return await estatus_estudiantes_service.update_estatus_estudiante(estatus_id, estatus_data)
