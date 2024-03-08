from fastapi import FastAPI
from app.controllers import user_controller
from app.database import Base, engine  

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/people", tags=["people"])