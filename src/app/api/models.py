from pydantic import conint, constr
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://hello_fastapi:hello_fastapi@db/hello_fastapi_dev')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(declarative_base):
     pass

class DoctorSchema(Base):
     __tablename__ = "doctors"

     doctor_id = Column(Integer,nullable=False,unique=True,primary_key=True,autoincrement=True)
     name: Mapped[str] = mapped_column, String(30), constr(min_length=1)
     surname: Mapped[str] = mapped_column, String(30), constr(min_length=1)
     category: Mapped[int] = mapped_column, Integer
     speciality: Mapped[str] = mapped_column(String(30))

     def __repr__(self):
         return f'{self.doctor_id} {self.name} {self.surname} {self.category} {self.speciality}'

class DoctorDB(DoctorSchema):
    id: int

class ClientSchema(Base):
    __tablename__ = "clients"

    client_id = Column(Integer,nullable=False,unique=True,primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column, String(30), constr(min_length=1)
    surname: Mapped[str] = mapped_column, String(30), constr(min_length=1)
    email: Mapped[str] = mapped_column, String(30)
    age: Mapped[int] = mapped_column, Integer, conint(gt=0)
    phone: Mapped[int] = mapped_column(unique=True, min_length=7, max_length=20)

    def __repr__(self):
        return f'{self.client_id} {self.name} {self.surname} {self.email} {self.age} {self.phone}'

class ClientDB(ClientSchema):
    id: int

class RoomSchema(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer,nullable=False,unique=True,primary_key=True,autoincrement=True)
    number: Mapped[int] = mapped_column, Integer

    def __repr__(self):
        return f'{self.room_id} {self.number}'

class RoomDB(RoomSchema):
    id: int

class AppointmentSchema(Base):
    __tablename__ = "appointments"

    appointment_id = Column(Integer,nullable=False,unique=True,primary_key=True,autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))
    room_id = Column(Integer, ForeignKey('room.room_id'))
    client_id = Column(Integer, ForeignKey('client.client_id'))
    doctor = relationship('Doctor', backref='appointments_doctor', lazy='subquery')
    room = relationship('Room', backref='appointments_room', lazy='subquery')
    client = relationship('Client', backref='appointments_client', lazy='subquery')

    def __repr__(self):
        return f'{self.appointment_id} {self.doctor_id} {self.room_id} {self.client_id}'

class AppointmentDB(AppointmentSchema):
    id: int
