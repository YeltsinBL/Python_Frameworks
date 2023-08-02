"""Usuarios"""
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    """Clase Usuario"""
    name:str
    alias:str
    age:int

users = [User(name="Yeltsin",alias="BL",age=24),
         User(name="Yelt",alias="B",age=22),
         User(name="Yel",alias="",age=20)]

@app.get("/users")
async def users_list():
    """Lista usuarios"""
    return users
@app.get("/users/{edad}")
async def users_path(edad:int, response:Response):
    """Lista usuarios por edad"""
    lista = search_user(edad=edad)
    if isinstance(lista, dict):
        response.status_code = status.HTTP_204_NO_CONTENT
        return lista
    return lista
@app.get("/userquery/")
async def users_query(edad: int):
    """Lista usuarios por edad"""
    lista = search_user(edad=edad)
    if isinstance(lista, dict):
        raise HTTPException(204)
    return lista
@app.get("/userquerys/")
async def users_querys(edad: int, alias:str=""):
    """Lista usuarios por edad"""
    return search_user_(alias=alias, edad=edad)

@app.post("/user/")
async def user_create(user: User):
    """Guardar usuarios"""
    user_filter = filter(lambda user_: user_.name == user.name, users)
    if len(list(user_filter))>0:
        raise HTTPException(404,"El usuario ya existe")
    users.append(user)

@app.put("/user/")
async def user_update(user: User):
    """Modificar usuarios"""
    editado = False
    for clave, valor in enumerate(users):
        if valor.name == user.name and editado is False:
            users[clave] = user
            editado = True
    if editado is False:
        return {"error": "Usuario inexistente"}

@app.delete("/user/")
async def user_delete(nombre:str):
    """Modificar usuarios"""
    editado = False
    for clave, valor in enumerate(users):
        if valor.name == nombre and editado is False:
            del users[clave]
            editado = True
    if editado is False:
        return {"error": "Usuario inexistente"}

# region Funciones
def search_user(edad:int):
    """Buscar usuario"""
    try:
        user = filter(lambda user_: user_.age == edad, users)
        return list(user)[0]
    except Exception:
        return {"error": "no encontró datos"}
def search_user_(alias:str, edad:int):
    """Buscar usuario"""
    try:
        user = filter(lambda user_: user_.age == edad and\
                      (alias.lower() =="" or user_.alias.lower()==alias.lower()), users)
        return list(user)[0]
    except Exception:
        return {"error": "no encontró datos"}
# endregion
