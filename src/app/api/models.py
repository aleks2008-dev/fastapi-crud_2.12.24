from pydantic import BaseModel


class DoctorSchema(BaseModel):
    name: str
    surname: str
    category: int
    speciality: str

class DoctorDB(DoctorSchema):
    id: int

class ClientSchema(BaseModel):
    name: str
    surname: str
    email: str
    age: int
    phone: int

class ClientDB(ClientSchema):
    id: int

class RoomSchema(BaseModel):
    number: int

class RoomDB(RoomSchema):
    id: int

class AppointmentSchema(BaseModel):
    date: int

class AppointmentDB(AppointmentSchema):
    id: int