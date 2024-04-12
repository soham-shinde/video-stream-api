from fastapi import APIRouter, HTTPException

from app.controllers import user
from app.models import UserRegister, UserLogin

router = APIRouter()


@router.post("/register/")
def register_user(user_data: UserRegister):
    created_user = user.register_user(user_data)
    if created_user:
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=400, detail="User with this email already exists")


@router.post("/login/")
def login_user(user_data: UserLogin):
    user_info = user.login_user(user_data)
    if user_info:
        return {"message": "Login successful", "user_info": user_info}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
