from fastapi import FastAPI
app = FastAPI()

BOOKS = [{"Title": "Rachel Wilkerson", "Author": "Raya Burton", "Genre": "Priscilla Newton"}, {"Title": "Libby Hardy", "Author": "Caldwell Burch", "Genre": "Althea Conley"}, {"Title": "Lana Whitehead","Author": "Beau Solomon", "Genre": "Shellie Mcleod"}, {"Title": "Naomi Murray", "Author": "Adam Ayala", "Genre": "Kessie Haney"}, {"Title": "Tamekah Dunlap", "Author": "Haviva Roy", "Genre": "Piper Mooney"}]


@app.get("/")
async def home():
    return BOOKS

@app.get("/books/{title}")
async def get_book(title: str):
    for book in BOOKS:
        if book.get('Title').casefold()==title.casefold():
            return book
        
