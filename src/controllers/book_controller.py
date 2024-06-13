from flask import Blueprint, request, jsonify
from models.book import Book
from app import db

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        edition=data.get('edition'),
        year_of_publication=data.get('year_of_publication')
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@bp.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books])

@bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.author = data['author']
    book.edition = data.get('edition')
    book.year_of_publication = data.get('year_of_publication')
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})
