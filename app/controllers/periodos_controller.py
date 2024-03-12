from fastapi import APIRouter, Depends
from app.services.periodos_service import PeriodosService
from app.models.periodos import PeriodosIn, PeriodosOut, PeriodosDelete, PeriodosUpdate

router = APIRouter()
periodos_service = PeriodosService()

@router.post("/", response_model=PeriodosOut)
async def create_periodo(periodo_data: PeriodosIn):
    return await periodos_service.create_periodo(periodo_data)

@router.get("/{periodo_id}", response_model=PeriodosOut)
async def get_periodo(periodo_id: int):
    return await periodos_service.get_periodo(periodo_id)

@router.delete("/{periodo_id}", response_model=PeriodosOut)
async def delete_periodo(periodo_id: int):
    return await periodos_service.delete_periodo(periodo_id)

@router.put("/{periodo_id}", response_model=PeriodosOut)
async def update_periodo(periodo_id: int, periodo_data: PeriodosIn):
    return await periodos_service.update_periodo(periodo_id, periodo_data)
