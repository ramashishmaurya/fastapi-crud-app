# Book Management CRUD API

A RESTful CRUD API built using FastAPI, SQLAlchemy, and PostgreSQL for managing book records.

## Features

- Create a new book
- Read all books
- Read a single book by ID
- Update existing book details
- Delete books
- PostgreSQL database integration
- SQLAlchemy ORM support
- FastAPI automatic interactive documentation
- Request validation using Pydantic

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books` | Get all books |
| GET | `/books/{id}` | Get book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update a book |
| DELETE | `/books/{id}` | Delete a book |

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
