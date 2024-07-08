from typing import TypedDict
from pydantic import BaseModel, field_validator, model_validator

from .utils import get_user_by_email
import re

class RegisterData(BaseModel):
    name: str
    surname: str
    email: str
    password: str

    @field_validator('email')
    def email_validator(cls, v):
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', v) is None:
            raise ValueError('Invalid email')
        if get_user_by_email(v):
            raise ValueError('User already exists')
        return v

class LoginData(BaseModel):
    email: str
    password: str

class RegisterDataFunc(TypedDict):
    name: str
    surname: str
    email: str
    password: str