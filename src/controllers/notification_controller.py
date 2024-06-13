# controllers/notification_controller.py
from flask import Blueprint, jsonify

notification_bp = Blueprint('notification_bp', __name__, url_prefix='/notifications')

@notification_bp.route('/', methods=['GET'])
def get_notifications():
    # Simulação de notificações
    notifications = [
        {"message": "You have books to return soon", "type": "warning"},
        {"message": "Book returned late", "type": "alert"}
    ]
    return jsonify(notifications)
