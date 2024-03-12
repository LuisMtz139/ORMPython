from app.models.user import UserIn, UserOut, UserInDB
from app.database import SessionLocal
from fastapi import HTTPException

class UserService:
    def __init__(self):
        self.db = SessionLocal()

    async def create_user(self, user_data: UserIn):
        db_user = UserInDB(**user_data.dict()) 
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserOut(**db_user.__dict__)  

    async def get_user(self, user_id: int):
        user = self.db.query(UserInDB).filter(UserInDB.id == user_id).first()  
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserOut(**user.__dict__) 
    
    async def delete_user(self, user_id: int):
        user = self.db.query(UserInDB).filter(UserInDB.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(user)
        self.db.commit()
        return UserOut(**user.__dict__)

    async def update_user(self, user_id: int, user_data: UserIn):
        user = self.db.query(UserInDB).filter(UserInDB.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        for var, value in user_data:
            setattr(user, var, value)
        self.db.commit()
        self.db.refresh(user)
        return UserOut(**user.__dict__)