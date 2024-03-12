from fastapi import APIRouter, Depends
from app.services.docente_service import DocenteService
from app.models.docentes import DocentesOut,DocentesIn,DocentesInDB

router = APIRouter()
docenteService = DocenteService()


@router.post("/", response_model=DocentesOut)
async def create_docente(docente_data: DocentesIn):
    return await docenteService.create_docente(docente_data)

@router.get("/{docente_id}", response_model=DocentesOut)
async def get_docente(docente_id: int):
    return await docenteService.get_docente(docente_id)

@router.delete("/{docente_id}", response_model=DocentesOut)
async def delete_docente(docente_id: int):
    return await docenteService.delete_docente(docente_id)

@router.put("/{docente_id}", response_model=DocentesOut)
async def update_docente(docente_id: int, docente_data: DocentesIn):
    return await docenteService.update_docente(docente_id, docente_data)

