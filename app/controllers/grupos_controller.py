from fastapi import APIRouter
from app.services.grupos_service import GruposService
from app.models.grupos import GruposIn, GruposOut, GruposDelete, GruposUpdate

router = APIRouter()
grupos_service = GruposService()

@router.post("/", response_model=GruposOut)
async def create_grupos(grupos_data: GruposIn):
    return await grupos_service.create_grupos(grupos_data)

@router.get("/{grupos_id}", response_model=GruposOut)
async def get_grupos(grupos_id: int):
    return await grupos_service.get_grupos(grupos_id)

@router.delete("/{grupos_id}", response_model=GruposOut)
async def delete_grupos(grupos_id: int):
    return await grupos_service.delete_grupos(grupos_id)

@router.put("/{grupos_id}", response_model=GruposOut)
async def update_grupos(grupos_id: int, grupos_data: GruposUpdate):
    return await grupos_service.update_grupos(grupos_id, grupos_data)
