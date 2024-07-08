from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session

import os

DATABASE_URL = f'postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)

class Base(DeclarativeBase):
    pass