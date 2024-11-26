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

# Install dependencies and the package itself using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install

# Copy the rest of the application
COPY . /app

# Default command for the container
CMD ["poetry", "run", "data-collection"]