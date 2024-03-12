from fastapi import APIRouter, Depends
from app.services.asignaturas_service import AsignaturasService
from app.models.asignaturas import AsignaturasIn, AsignaturasOut

router = APIRouter()
asignaturasService = AsignaturasService()


@router.post("/", response_model=AsignaturasOut)
async def create_asignaturas(asignaturas_data: AsignaturasIn):
    return await asignaturasService.create_asignaturas(asignaturas_data)

@router.get("/{asignaturas_id}", response_model=AsignaturasOut)
async def get_asignaturas(asignaturas_id: int):
    return await asignaturasService.get_asignaturas(asignaturas_id)

@router.delete("/{asignaturas_id}", response_model=AsignaturasOut)
async def delete_asignaturas(asignaturas_id: int):
    return await asignaturasService.delete_asignaturas(asignaturas_id)

@router.put("/{asignaturas_id}", response_model=AsignaturasOut)
async def update_asignaturas(asignaturas_id: int, asignaturas_data: AsignaturasIn):
    return await asignaturasService.update_asignaturas(asignaturas_id, asignaturas_data)

