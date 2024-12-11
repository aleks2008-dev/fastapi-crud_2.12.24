import os
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

#engine = create_engine(DATABASE_URL)
#metadata = MetaData()
Base = declarative_base()

database = Database(DATABASE_URL)
