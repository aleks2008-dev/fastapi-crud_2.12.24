from app.api.models import DoctorSchema, ClientSchema, AppointmentSchema
from app.db import doctors, database, clients, appointments


async def post_doctors(payload: DoctorSchema):
    query = doctors.insert().values(name=payload.name, surname=payload.surname, category=payload.category, speciality=payload.speciality)
    return await database.execute(query=query)

async def post(payload: ClientSchema):
    query = clients.insert().values(name=payload.name, surname=payload.surname, email=payload.email, age=payload.age, phone=payload.phone)
    return await database.execute(query=query)

async def get_all_doctors():
    query = doctors.select()
    return await database.fetch_all(query=query)

async def get_all():
    query = clients.select()
    return await database.fetch_all(query=query)

async def get_doctors(id: int):
    query = doctors.select().where(id == doctors.c.id)
    return await database.fetch_one(query=query)

async def get(id: int):
    query = clients.select().where(id == clients.c.id)
    return await database.fetch_one(query=query)

async def put_doctors(id: int, payload: DoctorSchema):
    query = (
        doctors
        .update()
        .where(id == doctors.c.id)
        .values(name=payload.name, surname=payload.surname, category=payload.category, speciality=payload.speciality)
        .returning(doctors.c.id)
    )
    return await database.execute(query=query)

async def put(id: int, payload: ClientSchema):
    query = (
        clients
        .update()
        .where(id == clients.c.id)
        .values(name=payload.name, surname=payload.surname, email=payload.email, age=payload.age, phone=payload.phone)
        .returning(clients.c.id)
    )
    return await database.execute(query=query)

async def patch_doctors(id: int, payload: DoctorSchema):
    query = (
        doctors
        .update()
        .where(id == doctors.c.id)
        .values(name=payload.name, surname=payload.surname, category=payload.category, speciality=payload.speciality)
        .returning(doctors.c.id)
    )
    return await database.execute(query=query)

async def delete_doctor(id: int):
    query = doctors.delete().where(id == doctors.c.id)
    return await database.execute(query=query)

async def delete(id: int):
    query = clients.delete().where(id == clients.c.id)
    return await database.execute(query=query)