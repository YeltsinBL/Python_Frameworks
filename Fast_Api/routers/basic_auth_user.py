"""Autenticación Básica de Usuario con OAuth2"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


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
        "password": "123456"
    },
    "yeltsin": {
        "username": "yeltsin",
        "full_name": "yeltsin xd",
        "email": "yeltsin@xd.com",
        "disabled": True,
        "password": "654321"
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

async def current_user(token: str = Depends(oauth2)):
    """Usuario Actual"""
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

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
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def my_user(user: User = Depends(current_user)):
    """Credencial del Usuario"""
    return user
