# Trade Service API

A simple backend service for trade orders built with FastAPI, SQLAlchemy, and SQLite for local development. This service exposes REST APIs to create and retrieve trade orders and provides interactive API documentation.

## Features

- **POST /orders:** Create a new trade order.
- **GET /orders:** Retrieve a list of all trade orders.
- Auto-generated API documentation using **Swagger UI** and **Redoc**.

## Tech Stack

- **Backend:** FastAPI, Uvicorn
- **Database:** SQLite (for local development; easily swappable with PostgreSQL)
- **ORM:** SQLAlchemy
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions (for automated builds and deployments)

## Getting Started

### Prerequisites

- Python 3.9+ installed
- Git installed
- Virtual environment (recommended)
- Docker & Docker Compose installed (for containerization)
- (Optional) An AWS EC2 instance if deploying to production

### Project Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ayushhpatel/trade-service.git
   cd trade-service
