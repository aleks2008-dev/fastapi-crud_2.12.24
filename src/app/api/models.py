from pydantic import BaseModel, constr, conint
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ForeignKey
)
#from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

class Base(declarative_base):
     pass

class DoctorSchema(Base):
     __tablename__ = "doctors"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(constr(min_length=1, max_length=20), String(30))
     surname: Mapped[str] = mapped_column(constr(min_length=1, max_length=20), String(30))
     category: Mapped[int] = mapped_column(conint(ge=0), Integer(3))
     speciality: Mapped[str] = mapped_column(String(30))

class DoctorDB(DoctorSchema):
    id: int

class ClientSchema(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(constr(min_length=1, max_length=20), String(30))
    surname: Mapped[str] = mapped_column(constr(min_length=1, max_length=20), String(30))
    email: Mapped[str] = mapped_column(constr(unique=True, max_length=20), String(30))
    age: Mapped[int] = mapped_column(conint(ge=0), Integer(3))
    phone: Mapped[int] = mapped_column(unique=True, min_length=7, max_length=20)

class ClientDB(ClientSchema):
    id: int

class RoomSchema(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(conint(ge=0), Integer(3))

class RoomDB(RoomSchema):
    id: int

class AppointmentSchema(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))

class AppointmentDB(AppointmentSchema):
    id: int