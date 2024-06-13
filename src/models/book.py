from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    edition = db.Column(db.String(50), nullable=True)
    year_of_publication = db.Column(db.String(4), nullable=True)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Book {self.title}>'
