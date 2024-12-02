from fastapi import APIRouter, HTTPException
from app.api import crud
from app.api.models import AppointmentDB, AppointmentSchema

router = APIRouter()


@router.post("/", response_model=AppointmentDB, status_code=201)
async def add_appointment(payload: AppointmentSchema):
    appointment_id = await crud.post(payload)

    response_object = {
        "id": appointment_id,
        "date": payload.date
    }
    return response_object

@router.get("/{id}/", response_model=AppointmentDB)
async def read_appointment(id: int ):
    appointment = await crud.get(id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@router.get("/", response_model=AppointmentDB)
async def read_all_appointments():
    return await crud.get_all()

@router.put("/{id}/", response_model=AppointmentDB)
async def update_appointment(payload: AppointmentSchema, id: int ):
    appointment = await crud.get(id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment_id = await crud.put(id, payload)

    response_object = {
        "id": appointment_id,
        "date": payload.date
    }
    return response_object

@router.delete("/{id}/", response_model=AppointmentDB)
async def delete_appointment(id: int ):
    appointment = await crud.get(id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    await crud.delete(id)

    return appointment