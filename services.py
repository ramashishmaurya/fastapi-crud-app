from model import Book
from sqlalchemy.orm import session
from schemas import CreatBook

def create_book(db :session , data:CreatBook):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db:session):
    return db.query(Book).all()

def get_book(db:session , book_id:int):
    return db.query(Book).filter(Book.id ==book_id).first()



