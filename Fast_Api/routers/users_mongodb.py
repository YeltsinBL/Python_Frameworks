"""CRUD de Usuarios usando MongoDB Local"""
from fastapi import APIRouter, Response, status, HTTPException
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/usersmongodb",
                   tags=["usersmongodb"],
                   responses={404:{"message":"No encontrado"}})
DB_USERS= db_client.local.users

# region Gets
@router.get("/", response_model=list[User])
async def users_list():
    """Lista usuarios"""
    return users_schema(DB_USERS.find())
@router.get("/{id}", response_model=User)
async def users_path(id:str, response:Response):
    """Lista usuarios por Id"""
    lista = search_user_by("_id", ObjectId(id))
    if isinstance(lista, dict):
        response.status_code = status.HTTP_204_NO_CONTENT
        return lista
    return lista
@router.get("/userquery/", response_model=User)
async def users_query(id: str):
    """Lista usuarios por Id"""
    lista = search_user_by("_id", ObjectId(id))
    if isinstance(lista, dict):
        raise HTTPException(status.HTTP_204_NO_CONTENT)
    return lista
# endregion

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user_create(user: User):
    """Guardar usuarios"""
    if isinstance(search_user_by("name", user.name), User):
    # if type(search_user_by_name(user.name)) == User:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"El usuario ya existe")

    user_dict = dict(user)
    # Eliminar el Id para que lo cree automáticamente MongoDB
    del user_dict["id"]
    # obtenemos el Id creador
    id_usuario = DB_USERS.insert_one(user_dict).inserted_id
    # obtenemos el registro por el Id
    new_user = user_schema(DB_USERS.find_one({"_id":id_usuario}))

    return User(**new_user)

@router.put("/")
async def user_update(user: User):
    """Modificar usuarios"""
    user_edit = dict(user)
    del user_edit["id"]

    try:
        # DB_USERS.find_one_and_replace({"_id":ObjectId(user.id)}, user_edit)
        DB_USERS.find_one_and_update({"_id":ObjectId(user.id)},
                                                  {"$set": dict(user_edit)}
                                                  )
        return search_user_by("_id",ObjectId(user.id))
    except:
        return {"error": "Usuario inexistente"}

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user_delete(id:str):
    """Eliminar usuario"""
    eliminado = DB_USERS.find_one_and_delete({"_id":ObjectId(id)})

    if not eliminado:
        return {"error": "Usuario no encontrado"}

# region Funciones
def search_user_by(field:str, value):
    """Buscar usuario por """
    try:
        user = user_schema(DB_USERS.find_one({field:value}))
        return User(**user)
    except Exception:
        return {"error": "no encontró datos"}
# endregion
