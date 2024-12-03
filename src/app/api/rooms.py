from fastapi import APIRouter, HTTPException
from app.api import crud
from app.api.models import DoctorDB, DoctorSchema
from typing import List

router = APIRouter()


@router.post("/", response_model=DoctorDB, status_code=201)
async def add_room(payload: DoctorSchema):
    doctor_id = await crud.post_doctors(payload)

    response_object = {
        "id": doctor_id,
        "name": payload.name,
        "surname": payload.surname,
        "category": payload.category,
        "speciality": payload.speciality,
    }
    return response_object

@router.get("/{id}/", response_model=DoctorDB)
async def read_room(id: int ):
    doctor = await crud.get_doctors(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.get("/", response_model=List[DoctorDB])
async def read_all_doctors():
    return await crud.get_all_doctors()


@router.put("/{id}/", response_model=DoctorDB)
async def update_doctor(id: int, payload: DoctorSchema):
    doctor = await crud.get_doctors(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor_id = await crud.put_doctors(id, payload)

    response_object = {
        "id": doctor_id,
        "name": payload.name,
        "surname": payload.surname,
        "category": payload.category,
        "speciality": payload.speciality,
    }
    return response_object

@router.patch("/{id}/", response_model=DoctorDB)
async def update_doctor_patch(id: int, payload: DoctorSchema):
    doctor = await crud.get_doctors(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor_id = await crud.patch_doctors(id, payload)

    response_object = {
        "id": doctor_id,
        "name": payload.name,
        "surname": payload.surname,
        "category": payload.category,
        "speciality": payload.speciality,
    }
    return response_object

@router.delete("/{id}/", response_model=DoctorDB)
async def delete_doctor(id: int ):
    doctor = await crud.delete_doctor(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    await crud.delete_doctor(id)

    return doctor