from pydantic import BaseModel

class BookBase(BaseModel):
    title :str 
    description:str 
    author:str 
    year :int

class CreatBook(BookBase):
    pass

class Book(BookBase):
    id :int 

    class config:
        from_attribute = True
        
