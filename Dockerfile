# Use an official Python image as the base image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file to install dependencies.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose port 8000 for the app.
EXPOSE 8000

# Command to run the FastAPI application with uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
