from flask import Blueprint, request, jsonify

bp = Blueprint('notifications', __name__, url_prefix='/notifications')

@bp.route('/', methods=['GET'])
def get_notifications():
    # Simulação de notificações
    notifications = [
        {"message": "You have books to return soon", "type": "warning"},
        {"message": "Book returned late", "type": "alert"}
    ]
    return jsonify(notifications)
