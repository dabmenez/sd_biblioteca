from app import db
from models.book import Book
from models.student import Student
from models.loan import Loan
from models.user import User

def init_db():
    db.create_all()
