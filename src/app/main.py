from fastapi import FastAPI
from app.api import doctors, clients, appointments, rooms
from app.db import database, engine, metadata
from contextlib import asynccontextmanager

metadata.create_all(engine)

#app = FastAPI()


#@app.on_event("startup")
#async def startup():
    #await database.connect()


#@app.on_event("shutdown")
#async def shutdown():
    #await database.disconnect()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])