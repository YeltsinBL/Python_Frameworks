"""Api de Productos"""
from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}})

products_list=["Producto 1", "Producto 2", "Producto 3"]

@router.get("/")
async def products():
    """Lista de todos los productos"""
    return products_list

@router.get("/{id}")
async def products_nro(id_product:int):
    """Lista de todos los productos"""
    return products_list[id_product]
