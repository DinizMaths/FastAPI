from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

from typing import Optional


class Book:
  id: int
  title: str
  author: str
  description: str
  rating: int
  published_date: int

  def __init__(self, id, title, author, description, rating, published_date):
    self.id             = id
    self.title          = title
    self.author         = author
    self.description    = description
    self.rating         = rating
    self.published_date = published_date

class BookRequest(BaseModel):
  id: Optional[int]   = Field(title="id is not needed")
  title: str          = Field(min_length=3)
  author: str         = Field(min_length=2)
  description: str    = Field(min_length=1, max_length=100)
  rating: int         = Field(ge=0, le=5) # 0 <= x <= 5
  published_date: int = Field(ge=1900)

  class Config:
    schema_extra = {
      "example": {
        "title": "A new book",
        "author": "codingwithroby",
        "description": "A new description",
        "rating": 5,
        "published_date": 2019
      }
    }


BOOKS = [
  Book(0, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
  Book(1, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!',     5, 2030),
  Book(2, 'Master Endpoints',     'codingwithroby', 'A awesome book!',   5, 2029),
  Book(3, 'HP1',                  'Author 1',       'Book Description',  2, 2028),
  Book(4, 'HP2',                  'Author 2',       'Book Description',  3, 2027),
  Book(5, 'HP3',                  'Author 3',       'Book Description',  1, 2026)
]

app = FastAPI()


@app.get("/")
async def home():
  return "Books 2"

@app.get("/books")
async def read_all_books():
  return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(ge=0)):
  for book in BOOKS:
    if book.id == book_id:
      return book

@app.get("/books/")
async def read_book_by_rating(book_rating: int):
  books = []

  for book in BOOKS:
    if book.rating == book_rating:
      books.append(book)
  
  return books

@app.get("/book/publish/")
async def read_books_by_publish_date(published_date: int):
  books = []

  for book in BOOKS:
    if book.published_date == published_date:
      books.append(book)
  
  return books

@app.post("/create-book")
async def create_book(book_request: BookRequest):
  new_book = Book(**book_request.dict())

  BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
  book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
  
  return book

@app.put("/books/update_books")
async def update_book(book: BookRequest):
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book.id:
      BOOKS[i] = book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(ge=0)):
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book_id:
      BOOKS.pop(i)

      break