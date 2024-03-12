from fastapi import APIRouter
from app.services.planes_service import PlanesService
from app.models.planes import PlanesIn, PlanesOut, PlanesDelete, PlanesUpdate

router = APIRouter()
planes_service = PlanesService()

@router.post("/", response_model=PlanesOut)
async def create_planes(planes_data: PlanesIn):
    return await planes_service.create_planes(planes_data)

@router.get("/{planes_id}", response_model=PlanesOut)
async def get_planes(planes_id: int):
    return await planes_service.get_planes(planes_id)

@router.delete("/{planes_id}", response_model=PlanesOut)
async def delete_planes(planes_id: int):
    return await planes_service.delete_planes(planes_id)

@router.put("/{planes_id}", response_model=PlanesOut)
async def update_planes(planes_id: int, planes_data: PlanesUpdate):
    return await planes_service.update_planes(planes_id, planes_data)
