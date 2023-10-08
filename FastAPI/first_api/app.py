from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

BOOKS = [{"Title": "Rachel Wilkerson", "Author": "Raya Burton", "Genre": "Action"}, {"Title": "Libby Hardy", "Author": "Caldwell Burch", "Genre": "Action"}, {"Title": "Lana Whitehead","Author": "Beau Solomon", "Genre": "Adventure"}, {"Title": "Naomi Murray", "Author": "Adam Ayala", "Genre": "Adventure"}, {"Title": "Tamekah Dunlap", "Author": "Haviva Roy", "Genre": "Adventure"}]

class Book(BaseModel):
    Title:str
    Author:str
    Genre:str

@app.get("/")
async def home():
    return BOOKS

@app.get("/books/{title}")
async def get_book(title: str):
    for book in BOOKS:
        if book.get('Title').casefold()==title.casefold():
            return book
        

@app.get("/books")
async def get_books_by_category(category: str):
    books_by_category=[]
    for book in BOOKS:
        if book.get("Genre").casefold()==category.casefold():
            books_by_category.append(book)
    
    return books_by_category

@app.get("/books/{author}")
async def get_books_by_author_and_category(author: str, category: str):
    books=[]
    for book in BOOKS:
        if book.get("Author").casefold()==author.casefold() and book.get("Genre").casefold()==category.casefold():
            books.append(book)
            
    return books

@app.post("/books/create_book")
async def create_book(new_book:Book):
    BOOKS.append(new_book)
    return BOOKS
    
@app.put("/books/update_book")
async def update_book(updated_book:Book):
    for (i,book) in enumerate(BOOKS):
        if BOOKS[i].get("Title").casefold()==updated_book.Title.casefold():
            BOOKS[i]=updated_book
        break

@app.delete("/books/delete_book/{title}")
async def delete_book(title: str):
    for (i,book) in enumerate(BOOKS):
        if BOOKS[i].get("Title").casefold()==title.casefold():
            del BOOKS[i]
            break