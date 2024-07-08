import uuid
from sqlalchemy import BIGINT, create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session, mapped_column

from datetime import datetime as dt, timezone as tz
from typing import Annotated

import os

DATABASE_URL = f'postgresql://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)

class Base(DeclarativeBase):
    pass

utcnow = lambda: dt.now(tz.utc)

intpk = Annotated[int, mapped_column(type_=BIGINT, primary_key=True)]
uuidpk = Annotated[str, mapped_column(primary_key=True, default=uuid.uuid4)]
created_at = Annotated[dt, mapped_column(default=utcnow)]
updated_at = Annotated[dt, mapped_column(default=utcnow, onupdate=utcnow)]