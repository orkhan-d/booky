from typing import Unpack

from src.modules.auth.util_schemas import RegisterDataFunc
from .models import User, session

import bcrypt

def hash_password(password: str):
    return bcrypt.hashpw(password, bcrypt.gensalt()) # type: ignore

def check_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password, hashed_password) # type: ignore

def get_user_by_email(email):
    return session.query(User).filter(User.email == email).first()

def create_user(**kwargs: Unpack[RegisterDataFunc]):
    user = User(name=kwargs['name'],
                surname=kwargs['surname'],
                email=kwargs['email'],
                password=hash_password(kwargs['password']))
    session.add(user)
    session.commit()
    return user