# services/book_service.py
from models.book import Book
from app import db

def add_book(data):
    new_book = Book(
        title=data['title'],
        author=data['author'],
        edition=data.get('edition'),
        year_of_publication=data.get('year_of_publication')
    )
    db.session.add(new_book)
    db.session.commit()
    return new_book

def get_books():
    return Book.query.all()

def update_book(id, data):
    book = Book.query.get_or_404(id)
    book.title = data['title']
    book.author = data['author']
    book.edition = data.get('edition')
    book.year_of_publication = data.get('year_of_publication')
    db.session.commit()
    return book

def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return book
