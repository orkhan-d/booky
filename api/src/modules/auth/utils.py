from typing import Unpack

from src.modules.auth.util_schemas import RegisterDataFunc
from .models import User, session


def get_user_by_email(email):
    return session.query(User).filter(User.email == email).first()


def create_user(**kwargs: Unpack[RegisterDataFunc]):
    user = User(name=kwargs['name'],
                surname=kwargs['surname'],
                email=kwargs['email'],
                password=kwargs['password'])
    session.add(user)
    session.commit()
    return user