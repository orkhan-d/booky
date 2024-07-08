from fastapi import APIRouter

from src.modules.auth.exceptions import InvalidCredentials
from .schemas import RegisterData, LoginData

from .utils import get_user_by_email, create_user

router = APIRouter(tags=["auth"], prefix="/auth")

@router.post("/register")
async def register(data: RegisterData):
    user = create_user(**data.model_dump())
    return user

@router.post("/login")
async def login(data: LoginData):
    user = get_user_by_email(data.email)
    if user is None or user.password != data.password:
        raise InvalidCredentials()
    return user