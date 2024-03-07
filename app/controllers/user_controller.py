# app/controllers/user_controller.py
from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.models.user import UserCreate, User

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=User)
async def create_user(user_data: UserCreate):
    return await user_service.create_user(user_data)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return await user_service.get_user(user_id)
