from fastapi import FastAPI, Body


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

@app.get("/books/{book_author}")
async def read_books_by_author(book_author: str):
  books_by_author = []

  for book in BOOKS:
    if book.get("author").casefold() == book_author.casefold():
      books_by_author.append(book)
    
  return books_by_author if len(books_by_author) > 0 else "Not Found"

@app.get("/books/")
async def read_book_by_category(book_category: str):
  books_by_category = []

  for book in BOOKS:
    if book.get("category").casefold() == book_category.casefold():
      books_by_category.append(book)
    
  return books_by_category if len(books_by_category) > 0 else "Not Found"

@app.get("/books/{book_author}/")
async def read_book_by_category(book_author: str, book_category: str):
  books = []

  for book in BOOKS:
    if book.get("author").casefold() == book_author.casefold() and book.get("category").casefold() == book_category.casefold():
      books.append(book)
    
  return books if len(books) > 0 else "Not Found"


@app.post("/books/create_book")
async def create_book(new_book=Body()):
  BOOKS.append(new_book)


@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
  for i in range(len(BOOKS)):
    if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
      BOOKS[i] = updated_book


@app.delete("/books/dete_book/{book_title}")
async def delete_book(book_title):
  for i, book in enumerate(BOOKS):
    if book.get("title").casefold() == book_title.casefold():
      BOOKS.pop(i)

      break