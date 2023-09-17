"""Esquemas de Datos"""
from db.client import ma

class UserSchema(ma.Schema):
    """Obtener los datos cuanto use este esquema"""
    class Meta:
        """Lista formateada en respuesta a las api"""
        fields = ('id','name', 'email')
