from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.models.user import UserIn, UserOut

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=UserOut)
async def create_user(user_data: UserIn):
    return await user_service.create_user(user_data)

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    return await user_service.get_user(user_id)


@router.delete("/{user_id}", response_model=UserOut)
async def delete_user(user_id: int):
    return await user_service.delete_user(user_id)


@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_data: UserIn):
    return await user_service.update_user(user_id, user_data)

