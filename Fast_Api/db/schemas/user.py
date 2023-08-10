"""Esquema del Usuario"""

def user_schema(user) -> dict:
    """Convertir lo obtenido de la BD al modelo de usuario"""
    return {"id":str(user["_id"]),
            "name": user["name"],
            "email": user["email"]}
def users_schema(users) -> list:
    """Convertir lo obtenido de la BD a una lista de usuarios"""
    return [user_schema(user) for user in users]
