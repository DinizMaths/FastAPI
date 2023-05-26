from fastapi import FastAPI


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


app = FastAPI()

@app.get("/")
async def home():
  return "Hello World!"

@app.get("/books")
async def read_all_books():
  return BOOKS

@app.get("/books/?title={book_title}")
async def read_book_by_title(book_title):
  for book in BOOKS:
    if book.get("title").casefold() == book_title.casefold():
      return book

@app.get("/books/?author={book_author}")
async def read_book_by_title(book_author):
  for book in BOOKS:
    if book.get("author").casefold() == book_author.casefold():
      return book

@app.get("/books/?category={book_category}")
async def read_book_by_title(book_author):
  for book in BOOKS:
    if book.get("category").casefold() == book_category.casefold():
      return book