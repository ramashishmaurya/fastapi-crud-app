from fastapi import FastAPI , Depends , HTTPException

import services , model , schemas
from db import get_db , engine

from sqlalchemy.orm import session

app = FastAPI()

@app.get("/books/" ,response_model=list[schemas.Book])
def get_all_books(db:session=Depends(get_db)):
    return services.get_books(db)

@app.get("/books/{id}" , response_description=schemas.Book)
def get_book_by_id(id=int , db:session=Depends(get_db)):
    book_queryset = services.get_book(db ,id) 
    if book_queryset:
        return book_queryset
    raise(HTTPException(status_code=404 , detail="invalid book_id provided"))


@app.post('/books' ,response_model=schemas.Book)
def create_new_book(book:schemas.CreatBook , db:session=Depends(get_db)):
    return services.create_book(db ,book)
