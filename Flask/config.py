"""Configuraciones"""
import os
from dotenv import load_dotenv

# busca el archivo .env para cargar las credenciales en el sitema
load_dotenv()

class Config:
    """Clase de configuración"""
    # Configuración a la BD
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI =f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}:3306/{os.environ['MYSQL_DATABASE']}"
