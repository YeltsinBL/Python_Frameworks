"""Init principal"""

from main import app
from db.client import db

# Crea las tablas
with app.app_context():
    db.init_app(app)
    db.create_all()

# inicia la aplicación
if __name__ =="__main__":
    app.run(debug=True)
