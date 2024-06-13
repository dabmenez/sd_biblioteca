# views/auth_view.py
from flask import Blueprint, render_template
from services.auth_service import get_user
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth_view_bp', __name__, url_prefix='/auth')

@auth_bp.route('/profile')
@jwt_required()
def profile_view():
    current_user = get_user()
    return render_template('profile.html', user=current_user)
