from flask import Blueprint, request, jsonify
from services.auth_service import register_user, authenticate_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register_view():
    data = request.get_json()
    new_user = register_user(data)
    return jsonify({'message': 'User registered successfully', 'user': new_user.as_dict()}), 201

@auth_bp.route('/login', methods=['POST'])
def login_view():
    data = request.get_json()
    user = authenticate_user(data)
    if user:
        access_token = create_access_token(identity={'username': user.username, 'is_admin': user.is_admin})
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_view():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200
