from fastapi import Body, FastAPI

app=FastAPI()

BOOKS= [
    {"title": "1984", "author": "George Orwell", "publication_year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": 1925},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "publication_year": 1951},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": 1813}
]

@app.get('/')
async def home():
    return BOOKS

@app.get("/get-book/{book_title}")
async def get_book(book_title:str):
    for book in BOOKS:
        if book.get("title").casefold()==book_title.casefold():
            return book
        
@app.get("/books/")
async def get_books_by_publication_year(publication_year:str):
    books_to_return=list()
    for book in BOOKS:
        if book.get("publication_year")==int(publication_year):
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    try:
        BOOKS.append(new_book)
        return("Book created")
    except:
        return("Error occurred")
    
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in  range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==book_title.casefold():
            BOOKS.pop(i)
            break