import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# For local development, you can switch to SQLite if DATABASE_URL is not set.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./orders.db"  # Local SQLite database file
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
