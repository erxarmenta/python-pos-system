from sqlalchemy.orm import Session
from python_pos_system.core.security import verify_password, hash_password, create_access_token
from .model import User
from .schemas import UserRegister, UserLogin, TokenResponse
from fastapi import HTTPException, status

EMAIL_PATTERN = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
PASSWORD_PATTERN = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"


class AuthSerice:
    @staticmethod
    async def register(db: Session, user_data: UserRegister) -> TokenResponse:
        # 1. Verify credentials with regex
        
        # 2. Verify email exists
        
        # 3. Hash password
        
        # 4. Save user
        
        # 5. Create Token
        #return TokenResponse(access_token=access_token, token_type="bearer")
        return 0