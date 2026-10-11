from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from python_pos_system.core.database import get_db
from .service import AuthService
from .schemas import UserRegister, UserLogin, TokenResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    return await AuthService.register(db, user_data)

@router.post("/login")
async def login():
    return {"message": "Login successfully"}

@router.post("/logout")
async def logput():
    return {"message": "Logged out successfully"}

@router.post("/forgot-password")
async def forgot_password():
    return {"message": "Password successfully"}