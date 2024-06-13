# views/loan_view.py
from flask import Blueprint, render_template
from services.loan_service import get_loans

loan_bp = Blueprint('loan_view_bp', __name__, url_prefix='/loans')

@loan_bp.route('/')
def list_loans():
    loans = get_loans()
    return render_template('loan_list.html', loans=loans)
