from fastapi import APIRouter, Depends
from app.services.estatus_cardex_service import Estatus_cardexService
from app.models.user import UserIn, UserOut

router = APIRouter()
estatus_cardexService = Estatus_cardexService()

@router.post("/", response_model=UserOut)
async def create_estatus_cardex(estatus_cardex_data: UserIn):
    return await estatus_cardexService.create_estatus_cardex(estatus_cardex_data)

@router.get("/{estatus_cardex_id}", response_model=UserOut)
async def get_estatus_cardex(estatus_cardex_id: int):
    return await estatus_cardexService.get_estatus_cardex(estatus_cardex_id)

@router.delete("/{estatus_cardex_id}", response_model=UserOut)
async def delete_estatus_cardex(estatus_cardex_id: int):
    return await estatus_cardexService.delete_estatus_cardex(estatus_cardex_id)

@router.put("/{estatus_cardex_id}", response_model=UserOut)
async def update_estatus_cardex(estatus_cardex_id: int, estatus_cardex_data: UserIn):
    return await estatus_cardexService.update_estatus_cardex(estatus_cardex_id, estatus_cardex_data)