from fastapi import APIRouter
from app.services.calificaciones_service import CalificacionesService
from app.models.calificaciones import CalificacionesIn, CalificacionesOut, CalificacionesDelete, CalificacionesUpdate

router = APIRouter()
calificaciones_service = CalificacionesService()

@router.post("/", response_model=CalificacionesOut)
async def create_calificaciones(calificaciones_data: CalificacionesIn):
    return await calificaciones_service.create_calificaciones(calificaciones_data)

@router.get("/{calificaciones_id}", response_model=CalificacionesOut)
async def get_calificaciones(calificaciones_id: int):
    return await calificaciones_service.get_calificaciones(calificaciones_id)

@router.delete("/{calificaciones_id}", response_model=CalificacionesOut)
async def delete_calificaciones(calificaciones_id: int):
    return await calificaciones_service.delete_calificaciones(calificaciones_id)

@router.put("/{calificaciones_id}", response_model=CalificacionesOut)
async def update_calificaciones(calificaciones_id: int, calificaciones_data: CalificacionesUpdate):
    return await calificaciones_service.update_calificaciones(calificaciones_id, calificaciones_data)
