import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database
#from sqlalchemy.orm import mapped_column

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
metadata = MetaData()
# SQLAlchemy


doctors = Table(
    "doctors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("category", Integer),
    Column("speciality", String(50)),
    #Column("created_date", DateTime, default=func.now(), nullable=False),
)
clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("surname", String(50)),
    Column("email", String(50), unique=True),
    Column("age", Integer),
    Column("phone", Integer, unique=True),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
appointments = Table(
    "appointments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("create_date", DateTime, default=func.now(), nullable=False),
    Column("room_id", Integer, foreign_key="room.id"),
    Column("doctor_id", Integer, foreign_key="doctor.id"),
    Column("client_id", Integer, foreign_key="client.id"),
)
rooms = Table(
    "rooms",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("number", Integer),
)
# databases query builder
database = Database(DATABASE_URL)