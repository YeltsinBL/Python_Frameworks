"""Principal"""

from flask_marshmallow import Marshmallow
from config import Config
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

print(Config.SQLALCHEMY_DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI']= Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=Config.SQLALCHEMY_TRACK_MODIFICATIONS # evitar que de errores

# SQLAlchemy(app)
Marshmallow(app)


# region INICIO TODO EN UNO

# from flask_marshmallow import Marshmallow
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column
# from flask import Flask , request, jsonify


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:mysql123@localhost:3306/flask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # evitar que de errores

# db = SQLAlchemy(app) # interactuar con la base de datos
# ma = Marshmallow(app) # esquema para la DB

# class User(db.Model):
#     """Clase Usuario"""
#     __tablename__ = "user"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(50))

#     def __init__(self, name, email )->None:
#         self.name = name
#         self.email = email
# with app.app_context():
#     db.create_all()

# class UserSchema(ma.Schema):
#     """Obtener los datos cuanto use este esquema"""
#     class Meta:
#         """Lista formateada en respuesta a las api"""
#         fields = ('id','name', 'email')

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

# # users = Blueprint('main', __name__)
# @app.route('/users', methods= ['POST'])
# def create_user():
#     """Create User"""
#     name = request.json['name']
#     email = request.json['email']
#     new_user = User(name,email)
#     db.session.add(new_user)
#     db.session.commit()
#     return user_schema.jsonify(new_user)

# @app.route('/users', methods=['GET'])
# def get_users():
#     """Obtener los usuarios"""
#     # obtener los datos
#     all_users = User.query.all()
#     # formatear los datos
#     result = users_schema.dump(all_users)
#     return jsonify(result)

# @app.route('/users/<id>', methods=['GET'])
# def get_user_by(id:int):
#     """Obtener usuario por Id"""
#     user = User.query.get(id)
#     return user_schema.jsonify(user)

# @app.route('/users/<id>', methods= ['PUT'])
# def update_user(id:int):
#     """Actualizar Usuario"""
#     user = User.query.get(id)
#     name = request.json['name']
#     email = request.json['email']
#     user.name = name
#     user.email = email
#     db.session.commit()
#     return user_schema.jsonify(user)

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id:int):
#     """Eliminar usuario por Id"""
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()
#     return user_schema.jsonify(user)

# if __name__ =="__main__":
#     app.run(debug=True)

# endregion
