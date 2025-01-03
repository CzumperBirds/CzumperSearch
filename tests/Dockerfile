FROM python:3.9-slim as python-base

RUN apt-get update && apt-get install -y \
    curl \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

FROM cypress/included:12.7.0 as cypress-base

FROM python-base

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

RUN apt-get update && apt-get install -y \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnotify-dev \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    xauth \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

COPY utils/requirements.txt /app/utils/
WORKDIR /app/utils
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

WORKDIR /app/frontend
RUN npm install && npx cypress install

WORKDIR /app

EXPOSE 8282

VOLUME [ "/var/run/docker.sock:/var/run/docker.sock" ]

CMD ["bash", "/app/e2e-search.sh"]