# views/notification_view.py
from flask import Blueprint, render_template

notification_bp = Blueprint('notification_view_bp', __name__, url_prefix='/notifications')

@notification_bp.route('/')
def list_notifications():
    # Simulação de notificações para renderização
    notifications = [
        {"message": "You have books to return soon", "type": "warning"},
        {"message": "Book returned late", "type": "alert"}
    ]
    return render_template('notification_list.html', notifications=notifications)
