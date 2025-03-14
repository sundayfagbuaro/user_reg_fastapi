from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from core.security import create_access_token
from db.session import get_db
from core.hashing import Hasher
from db.repository.login import get_user_by_email  # Create this function in db/repository/login.py
from db.repository.login import authenticate_user

#Create a router
router = APIRouter()



@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(detail="Incorrect username or password", status_code=status.HTTP_401_UNAUTHORIZED)
#    access_token = create_access_token(data={"sub":user.email})
#    return {"access_token":access_token, "token_type": "bearer"}
    return {f"Logged in successfully"}
