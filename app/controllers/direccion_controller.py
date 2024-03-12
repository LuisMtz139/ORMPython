from fastapi import APIRouter, Depends
from app.services.direccion_service import DireccionService
from app.models.direccion import DireccionIn, DireccionOut, DireccionInDB

router = APIRouter()
direccion_service = DireccionService()

@router.post("/", response_model=DireccionOut)
async def create_direccion(direccion_data: DireccionIn):
    return await direccion_service.create_direccion(direccion_data)

@router.get("/{direccion_id}", response_model=DireccionOut)
async def get_direccion(direccion_id: int):
    return await direccion_service.get_direccion(direccion_id)

@router.delete("/{direccion_id}", response_model=DireccionOut)
async def delete_direccion(direccion_id: int):
    return await direccion_service.delete_direccion(direccion_id)

@router.put("/{direccion_id}", response_model=DireccionOut)
async def update_direccion(direccion_id: int, direccion_data: DireccionIn):
    return await direccion_service.update_direccion(direccion_id, direccion_data)