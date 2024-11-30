# Use an official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1

# Install Poetry
RUN pip install --no-cache poetry==$POETRY_VERSION

# Set the working directory
WORKDIR /app

# Copy Poetry files first (to leverage Docker cache)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install

# Copy the rest of the application
COPY . /app

EXPOSE 8000

# Default command for the container
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
