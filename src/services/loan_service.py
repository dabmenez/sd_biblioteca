# services/loan_service.py
from models.loan import Loan
from models.book import Book
from models.student import Student
from app import db
from datetime import datetime, timedelta

def add_loan(data):
    book = Book.query.get_or_404(data['book_id'])
    student = Student.query.get_or_404(data['student_id'])
    if not book.available:
        raise ValueError('Book is not available')

    loan = Loan(
        book_id=book.id,
        student_id=student.id,
        due_date=datetime.utcnow() + timedelta(days=14)
    )
    book.available = False
    db.session.add(loan)
    db.session.commit()
    return loan

def get_loans():
    return Loan.query.all()

def return_loan(id):
    loan = Loan.query.get_or_404(id)
    book = Book.query.get_or_404(loan.book_id)
    loan.return_date = datetime.utcnow()
    book.available = True
    db.session.commit()
    return loan
