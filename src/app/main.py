from fastapi import FastAPI, Depends
from app.api import doctors, clients, appointments, rooms
from app.db import database, engine, metadata
from contextlib import asynccontextmanager
import asyncio

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - creating resources like database connection
    print("Starting up...")
    await asyncio.sleep(1)  # Simulating startup delay

    yield  # This line divides startup and shutdown

    # Shutdown - cleanup resources
    print("Shutting down...")
    await asyncio.sleep(1)  # Simulating shutdown delay

app.add_event_handler("lifespan", lifespan)

app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
