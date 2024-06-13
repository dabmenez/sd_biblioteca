# views/book_view.py
from flask import Blueprint, render_template
from services.book_service import get_books

book_bp = Blueprint('book_view_bp', __name__, url_prefix='/books')

@book_bp.route('/')
def list_books():
    books = get_books()
    return render_template('book_list.html', books=books)
