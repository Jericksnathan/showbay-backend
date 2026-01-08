# Showbay Task Manager Backend

This repository contains a backend service built as part of the  
**Showbay.io – Python Backend Engineer Take-Home Assessment**.

The application provides a RESTful API for managing tasks with full CRUD
(Create, Read, Update, Delete) functionality, PostgreSQL persistence, and
integration with an external API.

---

## 🚀 Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- pytest
- Uvicorn

---

## ✨ Features

- Create, retrieve, update, and delete tasks
- Each task contains:
  - UUID identifier
  - Title
  - Description
  - External summary (fetched from an external API)
- PostgreSQL database persistence
- Input validation using Pydantic
- Proper HTTP status codes and error handling
- Automated tests for all CRUD operations

---

## 🗂️ Project Structure

showbay_backend/
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # Database CRUD operations
│ ├── external_api.py # External API integration
│ ├── requirements.txt # Project dependencies
│ └── tests/
│ ├── test_tasks.py # CRUD API tests
│ └── conftest.py # Pytest configuration (import path setup)
├── .gitignore
├── README.md



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/Jericksnathan/showbay-backend.git
cd showbay-backend
2️⃣ Create and activate a virtual environment
bash

python -m venv venv
Windows


venv\Scripts\activate
3️⃣ Install dependencies


pip install -r app/requirements.txt
4️⃣ Configure environment variables
Create a .env file in the project root:

env

DATABASE_URL=postgresql://<username>:<password>@localhost:5432/taskdb
⚠️ Do not commit .env to version control.

▶️ Running the Application
bash

uvicorn app.main:app --reload
API documentation (Swagger UI):

arduino

http://127.0.0.1:8000/docs
🔌 API Endpoints
Method	Endpoint	Description
POST	/tasks	Create a new task
GET	/tasks/{id}	Retrieve a task by ID
PUT	/tasks/{id}	Update an existing task
DELETE	/tasks/{id}	Delete a task

🧪 Running Tests

pytest
Test Coverage
Task creation

Task retrieval

Task update

Task deletion

conftest.py is used to configure pytest so the application modules
can be imported correctly during testing.

🧠 Design Decisions & Trade-offs

UUIDs are used for task identifiers to ensure global uniqueness

Business logic is separated from API routes using a CRUD layer

External API calls are handled asynchronously

Minimal but meaningful test coverage to validate core functionality