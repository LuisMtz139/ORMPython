from fastapi import APIRouter, Depends
from app.services.personas_service import PersonasService
from app.models.personas import PersonasIn, PersonasOut, PersonasDelete, PersonasUpdate

router = APIRouter()
personas_service = PersonasService()

@router.post("/", response_model=PersonasOut)
async def create_persona(persona_data: PersonasIn):
    return await personas_service.create_persona(persona_data)

@router.get("/{persona_id}", response_model=PersonasOut)
async def get_persona(persona_id: int):
    return await personas_service.get_persona(persona_id)

@router.delete("/{persona_id}", response_model=PersonasOut)
async def delete_persona(persona_id: int):
    return await personas_service.delete_persona(persona_id)

@router.put("/{persona_id}", response_model=PersonasOut)
async def update_persona(persona_id: int, persona_data: PersonasIn):
    return await personas_service.update_persona(persona_id, persona_data)
