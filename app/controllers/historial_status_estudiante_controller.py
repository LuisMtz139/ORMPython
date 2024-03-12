from fastapi import APIRouter, Depends
from app.services.historial_status_estudiante_service import Historial_status_estudianteService
from app.models.historial_status_estudiante import Historial_status_estudianteIn, Historial_status_estudianteOut

router = APIRouter()
historial_status_estudianteService = Historial_status_estudianteService()

@router.post("/", response_model=Historial_status_estudianteOut)
async def create_historial_status_estudiante(historial_status_estudiante_data: Historial_status_estudianteIn):
    return await historial_status_estudianteService.create_historial_status_estudiante(historial_status_estudiante_data)

@router.get("/{historial_status_estudiante_id}", response_model=Historial_status_estudianteOut)
async def get_historial_status_estudiante(historial_status_estudiante_id: int):
    return await historial_status_estudianteService.get_historial_status_estudiante(historial_status_estudiante_id)

@router.delete("/{historial_status_estudiante_id}", response_model=Historial_status_estudianteOut)
async def delete_historial_status_estudiante(historial_status_estudiante_id: int):
    return await historial_status_estudianteService.delete_historial_status_estudiante(historial_status_estudiante_id)

@router.put("/{historial_status_estudiante_id}", response_model=Historial_status_estudianteOut)
async def update_historial_status_estudiante(historial_status_estudiante_id: int, historial_status_estudiante_data: Historial_status_estudianteIn):
    return await historial_status_estudianteService.update_historial_status_estudiante(historial_status_estudiante_id, historial_status_estudiante_data)
