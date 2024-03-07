# app/services/user_service.py
from app.models.user import UserCreate, User
from app.database import SessionLocal

class UserService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_user(self, user_data: UserCreate):
        db_user = User(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    async def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()