from fastapi import FastAPI
from app.api import doctors, clients, appointments, rooms
from .db import database, engine, metadata, Base
from .models import SessionLocal
from contextlib import asynccontextmanager
import asyncio

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    Base.metadata.create_all(bind=engine)  # Create tables
    yield  # This is where the app runs
    print("Shutting down...")
    await asyncio.sleep(1)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_event_handler("lifespan", lifespan)

app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
