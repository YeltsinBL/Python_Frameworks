"""Archivo Principal"""
from fastapi import FastAPI

app = FastAPI()

# Funciones Asíncronas
@app.get("/")
async def root():
    """Petición Get"""
    return {"message": "Hello World"}
@app.get("/{valor}/")
async def root_valor(valor:int):
    """Petición Get y parámetro"""
    return {"id":valor,"message": "Hello World"}
