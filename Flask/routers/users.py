"""Usuarios"""

from flask import request, jsonify, Blueprint
from db.client import db
from db.models.user import User
from db.schemas.user import UserSchema

user_bp = Blueprint('users', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/users', methods= ['POST'])
def create_user():
    """Create User"""
    name = request.json['name']
    email = request.json['email']
    new_user = User(name,email)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """Obtener los usuarios"""
    # obtener los datos
    all_users = User.query.all()
    # formatear los datos
    result = users_schema.dump(all_users)
    return jsonify(result)

@user_bp.route('/users/<id>', methods=['GET'])
def get_user_by(id:int):
    """Obtener usuario por Id"""
    user = User.query.get(id)
    return user_schema.jsonify(user)

@user_bp.route('/users/<id>', methods= ['PUT'])
def update_user(id:int):
    """Actualizar Usuario"""
    user = User.query.get(id)
    name = request.json['name']
    email = request.json['email']
    user.name = name
    user.email = email
    db.session.commit()
    return user_schema.jsonify(user)

@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id:int):
    """Eliminar usuario por Id"""
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)
