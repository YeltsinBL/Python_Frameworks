"""Autenticación Básica de Usuario con JWT"""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import jwt, JWTError
from passlib.context import CryptContext


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET_KEY = "f5ce4ad8c3b57d9f878fcaf909494d9f21dab9bae4874e61ece3325e09bf5c44"

router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    """Clase Usuario"""
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    """Clase Usuario BD"""
    password: str


users_db = {
    "yeltsinbl": {
        "username": "yeltsinbl",
        "full_name": "yeltsin bl",
        "email": "yeltsinbl@bl.com",
        "disabled": False,
        "password": "$2a$12$wkXskalKcdNefj4WZZKkZukmIAqKc3GV7t/RQpsqxZSjFKZNQujTW"
    },
    "yeltsin": {
        "username": "yeltsin",
        "full_name": "yeltsin xd",
        "email": "yeltsin@xd.com",
        "disabled": True,
        "password": "$2a$12$pmJDv3gVsLunLO6PqIyOCeCZH1nIuEOqqaAx4I7x6KRm0xQZocVAm"
    }
}

def search_user_db(username: str):
    """Buscar usuario por BD"""
    if username in users_db:
        return UserDB(**users_db[username])
    return None
def search_user(username: str):
    """Buscar usuario"""
    if username in users_db:
        return User(**users_db[username])
    return None

async def auth_user(token:str = Depends(oauth2)):
    """Buscar el usuario"""
    # exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Credenciales de autenticación inválidas",
    #         headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET_KEY,algorithms= [ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    """Usuario Actual"""
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """Iniciar Sesión"""
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_DURATION)
                    }

    return {"access_token": jwt.encode(access_token, SECRET_KEY, ALGORITHM),
            "token_type": "bearer"}
@router.get("/users/me")
async def my_user(user: User = Depends(current_user)):
    """Credencial del Usuario"""
    return user
