"""Archivo Principal"""
from fastapi import FastAPI
from routers import users, products, basic_auth_user

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(basic_auth_user.router)

# Funciones Asíncronas
@app.get("/")
async def root():
    """Petición Get"""
    return {"message": "Hello World"}
@app.get("/{valor}/")
async def root_valor(valor:int):
    """Petición Get y parámetro"""
    return {"id":valor,"message": "Hello World"}
