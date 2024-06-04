from datetime import datetime, timedelta
from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError, decode, encode
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session
from zoneinfo import ZoneInfo

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import TokenData
from fast_zero.settings import Settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

"""declare the route path that generates the token"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


Session = Annotated[Session, Depends(get_session)]
oauth2_scheme = Annotated[oauth2_scheme, Depends(oauth2_scheme)]


async def get_current_user(
    session: Session,
    token: oauth2_scheme,
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode(
            token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHM]
        )
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
        token_data = TokenData(username=username)
    except DecodeError:
        raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception

    user = session.scalar(
        select(User).where(User.email == token_data.username)
    )

    if user is None:
        raise credentials_exception

    return user


def create_access_token(data: dict):
    """Function to crreate the access token of each user

    Args:
        data (dict): _description_

    Returns:
        _type_: _description_
    """
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=Settings().ACCESS_TOKEN_EXPIRES_AT
    )
    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        to_encode, Settings().SECRET_KEY, algorithm=Settings().ALGORITHM
    )

    return encoded_jwt


def get_password_hash(password: str):
    """Function to get the password hash

    Args:
        password (str): _description_

    Returns:
        _type_: _description_
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
