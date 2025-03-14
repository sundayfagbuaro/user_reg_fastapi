from typing import Optional
from jose import jwt
from datetime import datetime, timedelta

from core.config import settings


def create_access_token(data: dict):
        to_encode = data.copy
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRED_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
