from pydantic import BaseModel, constr, conint

class DoctorSchema(BaseModel):
    name: constr(min_length=1, max_length=20)
    surname: constr(min_length=1, max_length=20)
    category: conint(ge=0)
    speciality: str

class DoctorDB(DoctorSchema):
    id: int

class ClientSchema(BaseModel):
    name: constr(min_length=1, max_length=20)
    surname: constr(min_length=1, max_length=20)
    email: str
    age: conint(ge=0)
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