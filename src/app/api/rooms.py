from fastapi import APIRouter, HTTPException
from app.api import crud
from app.api.models import RoomDB, RoomSchema
from typing import List

router = APIRouter()


@router.post("/", response_model=RoomDB, status_code=201)
async def add_room(payload: RoomSchema):
    room_id = await crud.post_rooms(payload)

    response_object = {
        "id": room_id,
        "number": payload.number,
    }
    return response_object

@router.get("/{id}/", response_model=RoomDB)
async def read_room(id: int ):
    room = await crud.get_rooms(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.get("/", response_model=List[RoomDB])
async def read_all_rooms():
    return await crud.get_all_rooms()


@router.put("/{id}/", response_model=RoomDB)
async def update_room(id: int, payload: RoomSchema):
    room = await crud.get_rooms(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    room = await crud.put_rooms(id, payload)

    response_object = {
        "id": room_id,
        "number": payload.number,
    }
    return response_object

@router.patch("/{id}/", response_model=RoomDB)
async def update_room_patch(id: int, payload: RoomSchema):
    room = await crud.get_rooms(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    room_id = await crud.patch_rooms(id, payload)

    response_object = {
        "id": room_id,
        "number": payload.number,
    }
    return response_object

@router.delete("/{id}/", response_model=RoomDB)
async def delete_room(id: int ):
    room = await crud.delete_room(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    await crud.delete_room(id)

    return room