from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import engine, get_db

# Create database tables (SQLite will do this automatically; 
# for PostgreSQL, it will check if tables exist and create them)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Book CRUD for Render")

@app.get("/")
def read_root():
    """
    Returns a welcome message.
    """
    return {"message": "Hello, welcome to the Book API!"}

@app.get("/hello")
def say_hello():
    """
    Returns a plain text 'Hello' response.
    """
    return PlainTextResponse("Hello")

@app.get("/health")
def health_check():
    """
    Health check endpoint for Render.
    """
    return {"status": "healthy"}

# --- Book CRUD Endpoints ---

@app.post("/books/", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book.
    """
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of books.
    """
    return crud.get_books(db=db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get a specific book by ID.
    """
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update details of a book.
    """
    db_book = crud.update_book(db=db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by ID.
    """
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
