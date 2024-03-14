from fastapi import FastAPI

from app.controllers import user_controller


from app.seeders import userSeeders

from app.database import Base, engine  

app = FastAPI()

Base.metadata.create_all(bind=engine)

userSeeders.seed_people(100) ##se hace el llamo a seeders user 

app.include_router(user_controller.router, prefix="/people", tags=["people"])





