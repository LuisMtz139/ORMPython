from fastapi import APIRouter, Depends
from app.services.cat_periodos_service import Cat_periodosService
from app.models.cat_periodos import Cat_periodosIn, Cat_periodosOut, Cat_periodosInDB

router = APIRouter()
cat_periodosService = Cat_periodosService()


@router.post("/", response_model=Cat_periodosOut)
async def create_cat_periodos(cat_periodos_data: Cat_periodosIn):
    return await cat_periodosService.create_cat_periodos(cat_periodos_data)

@router.get("/{cat_periodos_id}", response_model=Cat_periodosOut)
async def get_cat_periodos(cat_periodos_id: int):
    return await cat_periodosService.get_cat_periodos(cat_periodos_id)

@router.delete("/{cat_periodos_id}", response_model=Cat_periodosOut)
async def delete_cat_periodos(cat_periodos_id: int):
    return await cat_periodosService.delete_cat_periodos(cat_periodos_id)

@router.put("/{cat_periodos_id}", response_model=Cat_periodosOut)
async def update_cat_periodos(cat_periodos_id: int, cat_periodos_data: Cat_periodosIn):
    return await cat_periodosService.update_cat_periodos(cat_periodos_id, cat_periodos_data)
