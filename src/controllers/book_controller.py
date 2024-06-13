# controllers/book_controller.py
from flask import Blueprint, request, jsonify
from services.book_service import add_book, get_books, update_book, delete_book

book_bp = Blueprint('book_bp', __name__, url_prefix='/books')

@book_bp.route('/', methods=['POST'])
def add_book_view():
    data = request.get_json()
    new_book = add_book(data)
    return jsonify({'message': 'Book added successfully', 'book': new_book.as_dict()}), 201

@book_bp.route('/', methods=['GET'])
def get_books_view():
    books = get_books()
    return jsonify([book.as_dict() for book in books])

@book_bp.route('/<int:id>', methods=['PUT'])
def update_book_view(id):
    data = request.get_json()
    updated_book = update_book(id, data)
    return jsonify({'message': 'Book updated successfully', 'book': updated_book.as_dict()})

@book_bp.route('/<int:id>', methods=['DELETE'])
def delete_book_view(id):
    deleted_book = delete_book(id)
    return jsonify({'message': 'Book deleted successfully', 'book': deleted_book.as_dict()})
