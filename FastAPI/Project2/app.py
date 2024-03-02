from fastapi import FastAPI,Body
from pydantic import BaseModel

app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:str
    
    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title =title
        self.author = author
        self.description = description
        self.rating = rating
        
class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    rating:int
    description:str
    
    
BOOKS=[
    Book(1,"Computer science pro","Cody","nice book",5),
    Book(1,"FastAPI tutorial","Cody rhodes","very nice book",4),
    Book(1,"LOTR1","J.R.R. Tolkien","good and nice book",4),
    Book(1,"LOTR2","J.R.R. Tolkien","good and nice book",5),
    Book(1,"LOTR3","J.R.R. Tolkien","good and nice book",3),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(new_book)