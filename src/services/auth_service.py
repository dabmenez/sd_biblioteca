# services/auth_service.py
from models.user import User
from app import db, bcrypt

def register_user(data):
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password, is_admin=data.get('is_admin', False))
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        return user
    return None

def get_user():
    from flask_jwt_extended import get_jwt_identity
    current_user_identity = get_jwt_identity()
    user = User.query.filter_by(username=current_user_identity['username']).first()
    return user
