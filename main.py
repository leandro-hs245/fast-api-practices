from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "category": "Fiction",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Fiction",
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "category": "Dystopian Fiction",
    },
]


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = next((book for book in BOOKS if book["id"] == book_id), None)
    return book


@app.post("/books")
async def create_book(book: dict = Body(...)):
    new_book = {
        "id": len(BOOKS) + 1,
        "title": book["title"],
        "author": book["author"],
        "category": book["category"],
    }
    BOOKS.append(new_book)
    return new_book


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: dict = Body(...)):
    existing_book = next((b for b in BOOKS if b["id"] == book_id), None)
    if existing_book:
        existing_book.update(
            {
                "title": book.get("title", existing_book["title"]),
                "author": book.get("author", existing_book["author"]),
                "category": book.get("category", existing_book["category"]),
            }
        )
        return existing_book
    return {"error": "Book not found"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global BOOKS
    BOOKS = [book for book in BOOKS if book["id"] != book_id]
    return {"message": "Book deleted"}
