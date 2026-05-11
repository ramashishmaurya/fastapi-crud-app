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

def update_book(db:session , book:CreatBook , book_id):
    book_queryset = db.query(Book).filter(Book.id ==book_id).first()
    if book_queryset:
        for keys , value in book.model_dump().items():
            setattr(book_queryset ,keys ,value)
            db.commit()
            db.refresh(book_queryset)
    return book_queryset

def delete_book(db:session , id:int):
    book_queryset = db.query(Book).filter(Book.id ==id).first()
    if book_queryset:
        db.delete(book_queryset)
        db.commit()
    return book_queryset








