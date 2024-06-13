from flask import Blueprint, request, jsonify
from models.loan import Loan
from models.book import Book
from models.student import Student
from app import db
from datetime import datetime, timedelta

bp = Blueprint('loans', __name__, url_prefix='/loans')

@bp.route('/', methods=['POST'])
def add_loan():
    data = request.get_json()
    book = Book.query.get_or_404(data['book_id'])
    student = Student.query.get_or_404(data['student_id'])
    if not book.available:
        return jsonify({'message': 'Book is not available'}), 400

    loan = Loan(
        book_id=book.id,
        student_id=student.id,
        due_date=datetime.utcnow() + timedelta(days=14)
    )
    book.available = False
    db.session.add(loan)
    db.session.commit()
    return jsonify({'message': 'Loan added successfully'}), 201

@bp.route('/', methods=['GET'])
def get_loans():
    loans = Loan.query.all()
    return jsonify([loan.as_dict() for loan in loans])

@bp.route('/<int:id>/return', methods=['PUT'])
def return_loan(id):
    loan = Loan.query.get_or_404(id)
    book = Book.query.get_or_404(loan.book_id)
    loan.return_date = datetime.utcnow()
    book.available = True
    db.session.commit()
    return jsonify({'message': 'Loan returned successfully'})
