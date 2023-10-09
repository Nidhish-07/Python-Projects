from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()



class Book(BaseModel):
    "Class for book"
    id:int
    title:str
    author:str
    genre:str
    description:str
    rating:int

    def __init__(self,id, title, author, genre, description, rating):
        super().__init__(id=id, title=title, author=author, genre=genre, description= description, rating=rating)
        # self.id=id
        # self.title=title
        # self.author=author
        # self.genre=genre
        # self.description=description
        # self.rating=rating
        

BOOKS = [Book(1,"Python", "John Doe", "Python", "Python is the best language in the world",5),Book(2,"JavaScript", "John Doe", "JavaScript", "JavaScript is the best language in the",4),Book(3,"C++", "John Doe", "C++", "C plus plus is the best language in the world",3),Book(4,"C#", "John Doe", "C#", "C# is the best language in the world",3)]


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
    book=Book(**new_book.dict())
    BOOKS.append(book)
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