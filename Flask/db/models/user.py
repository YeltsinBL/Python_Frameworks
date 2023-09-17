"""Usuario"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.client import db

class User(db.Model):
    """Clase Usuario"""
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

    def __init__(self, name, email )->None:
        self.name = name
        self.email = email
