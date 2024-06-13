# controllers/loan_controller.py
from flask import Blueprint, request, jsonify
from services.loan_service import add_loan, get_loans, return_loan

loan_bp = Blueprint('loan_bp', __name__, url_prefix='/loans')

@loan_bp.route('/', methods=['POST'])
def add_loan_view():
    data = request.get_json()
    try:
        new_loan = add_loan(data)
        return jsonify({'message': 'Loan added successfully', 'loan': new_loan.as_dict()}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@loan_bp.route('/', methods=['GET'])
def get_loans_view():
    loans = get_loans()
    return jsonify([loan.as_dict() for loan in loans])

@loan_bp.route('/<int:id>/return', methods=['PUT'])
def return_loan_view(id):
    updated_loan = return_loan(id)
    return jsonify({'message': 'Loan returned successfully', 'loan': updated_loan.as_dict()})
