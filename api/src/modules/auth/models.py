from src.db.base import Base, uuidpk, created_at, session
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuidpk]

    name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    username: Mapped[str | None] = mapped_column()

    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    created_at: Mapped[created_at]