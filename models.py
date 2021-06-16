from datetime import datetime
from extensions import db


class BooksToRead(db.Model):

    __tablename__ = 'books_to_read'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, author, title) -> None:
        self.author = author
        self.title = title

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_book(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def add_book(cls, book):
        db.session.add(book)
        db.session.commit()

    @classmethod
    def delete_book(self, book):
        db.session.delete(book)
        db.session.commit()

    def __repr__(self) -> str:
        return f"{self.author} - {self.title}"


class FinishedBooks(db.Model):

    __tablename__ = 'finished_books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, author, title) -> None:
        self.author = author
        self.title = title

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_book(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def add_book(cls, book):
        db.session.add(book)
        db.session.commit()

    @classmethod
    def delete_book(self, book):
        db.session.delete(book)
        db.session.commit()

    def __repr__(self) -> str:
        return f"{self.author} - {self.title}"
