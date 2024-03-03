from fastapi import FastAPI,Body,Path
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:str
    published_date:int
    
    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title =title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date=published_date
        
class BookRequest(BaseModel):
    id:Optional[int]=Field(title="id is not required")
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(gt=-1,lt=6)
    rating:int=Field(min_length=1,max_length=100)
    published_date:int=Field(gt=1999,lt=2025)
    
    class Config:
        json_schema_extra={
            'example':{
                'title':"new book",
                'author':'cwh',
                'description':'average book',
                'rating':3,
                'published_date':2005
            }
        }
    
    
BOOKS=[
    Book(1,"Computer science pro","Cody","nice book",5,2001),
    Book(2,"FastAPI tutorial","Cody rhodes","very nice book",4,2002),
    Book(3,"LOTR1","J.R.R. Tolkien","good and nice book",4,2003),
    Book(4,"LOTR2","J.R.R. Tolkien","good and nice book",5,2004),
    Book(5,"LOTR3","J.R.R. Tolkien","good and nice book",3,2005),
]

def find_book_id(book:Book):
    if len(BOOKS) >0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/") 
async def read_book_by_rating(book_rating:int):
    book_to_read=list()
    for book in BOOKS:
        if book.rating==book_rating:
            book_to_read.append(book)
    return book_to_read

@app.get("/books/published/{published_date}")
async def read_book_by_published_date(published_date:int):
        books_to_read=list()
        for book in BOOKS:
            if book.published_date==published_date:
                books_to_read.append(book)
        return books_to_read
        
        
@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    
@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            
@app.delete("/books/{book.id}")
async def delete_book(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break