FROM python:3.13-slim AS builder

ENV POETRY_VERSION=1.8.4
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry export --without-hashes -o requirements.txt

FROM python:3.13-slim AS deploy

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

#Envs
ENV VAULT_TOKEN=${VAULT_TOKEN}
ENV VAULT_ADDR=${VAULT_ADDR}
ENV SECRET_PATH=${SECRET_PATH}
ENV ELASTIC_KEY=${ELASTIC_KEY}
ENV ELASTIC_VALUE=${ELASTIC_VALUE}

ENTRYPOINT ["/app/wait-for-elasticsearch.sh"]

CMD ["python", "src/data_storage_service.py"]
