"""Clase Usuario"""
from pydantic import BaseModel
class User(BaseModel):
    """Clase Usuario"""
    id:str | None
    name:str
    email:str
