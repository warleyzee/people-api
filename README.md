# 🚀 People API — FastAPI

A REST API built with **Python and FastAPI** to process people data from a CSV file, applying **clean architecture principles, automated testing, and professional Git workflows**.

This project was developed as a **technical pilot / coding exercise**, with a strong focus on **code quality, maintainability, and industry best practices**.

---

## 🛠️ Technologies & Tools

- **Python 3.12+**
- **FastAPI** — modern, high-performance web framework for APIs
- **Uvicorn** — ASGI server
- **Pandas** — data processing and analysis
- **Pydantic** — data validation and serialization
- **Pytest** — unit and integration testing
- **HTTPX** — HTTP client for API testing
- **Git & GitHub** — version control and professional workflow

---

## 🧱 Project Architecture

The project follows a clear **separation of concerns**, inspired by architectures commonly used in professional software teams:

app/
├── main.py # Application entry point
├── routes/ # API layer (endpoints)
├── services/ # Business logic
├── models/ # Data schemas (Pydantic)
tests/
├── test_routes.py # Integration tests
├── test_services.py # Unit tests
data/
└── people.csv # Data source


### Responsibility Separation
- **Routes** → handle HTTP requests and responses  
- **Services** → implement business rules and data processing  
- **Models** → define API input/output contracts  
- **Tests** → ensure correctness and prevent regressions  

---

## 📡 Available Endpoints

### 🔹 `GET /people/stats`

Returns statistics calculated from the CSV data.

**Example response:**
```json
{
  "oldest": ["Igor"],
  "youngest": ["Zeca"],
  "average_age": 46
}
```
## 🧪 Automated Testing

The project includes automated tests covering:

✅ Business logic (services)

✅ API endpoints (integration tests)

✅ API response contracts (schemas)

Start the API
uvicorn app.main:app --reload


The API will be available at:

http://127.0.0.1:8000


Interactive Swagger documentation:

http://127.0.0.1:8000/docs

## 👤 Author

Warley Souza
Backend / Python / API Development

This project was developed as a practical demonstration of skills in software engineering, API design, and modern Python development practices.

## 🎯 Why this project stands out

This repository demonstrates not only the ability to write working code, but also:

professional project structure

test-driven thinking

clear API design

industry-standard tooling

Exactly what companies look for in real-world backend projects.
