"""Archivo Principal"""
from fastapi import FastAPI
from routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)

# Funciones Asíncronas
@app.get("/")
async def root():
    """Petición Get"""
    return {"message": "Hello World"}
@app.get("/{valor}/")
async def root_valor(valor:int):
    """Petición Get y parámetro"""
    return {"id":valor,"message": "Hello World"}
