FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache poetry==1.8.4

ENV PYTHONPATH=/app:/app/src:$PYTHONPATH


WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
    && poetry install

COPY . /app

CMD ["poetry", "run", "python", "src/data_storage_service.py"]
