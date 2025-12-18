# User Service – Open Hearing Assignment

## Overview
This project implements a production-ready User Management Service using FastAPI, SQLAlchemy, and MySQL.  
It supports secure user creation, updates, pagination-based retrieval, authentication, soft deletes, and auditing.

---

## Tech Stack
- Python 3.10
- FastAPI
- SQLAlchemy + Alembic
- MySQL 8
- Docker & Docker Compose
- Pytest

---

## Features
- User CRUD APIs
- JWT-based authentication
- Password hashing (PBKDF2)
- Soft delete support
- Pagination for list APIs
- Unit & Integration tests
- Dockerized setup

---

## Database Design
Key considerations:
- Unique constraints on Email, Aadhaar, PAN
- Soft delete using `is_deleted` flag
- Audit fields: `created_at`, `updated_at`, `deleted_at`
- Indexed fields for performance

---

## Running the Application


## API will be available at:

http://localhost:8000

---
## Health check:

- GET /health
---
## Running Tests
- pytest
---
## Pain Points & Learnings
## Pain Points

- Handling differences between MySQL and SQLite during testing

- Password hashing compatibility on Windows

- Managing Alembic migrations cleanly

- Ensuring proper dependency management

## Learnings

- Designing production-grade database schemas

- Writing clean service & repository layers

- Importance of Docker for reproducibility

- Writing reliable unit and integration tests

- Handling real-world edge cases early
---
## Best Practices Followed

- Separation of concerns (API, Service, Repository layers)

- Secure password handling

- Environment-based configuration

- Frequent, meaningful Git commits

- Defensive error handling

- Clean, readable code structure
---
### Using Docker (Recommended)
```bash
docker compose build
docker compose up
