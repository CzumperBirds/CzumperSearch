# Infrastructure

This folder contains Docker Compose configurations for different environments in the project.

## Files

- **`docker-compose.dev.yml`**  
  Infrastructure stack for local development. This setup is designed to be simple and straightforward for developers to use on their local machines.

- **`docker-compose.test.yml`**  
  Configuration for the test environment.

- **`docker-compose.prod.yml`**  
  Configuration for the production environment.

---

## How to Launch the Development Environment

To launch the local development environment, run the following command:

```bash
docker compose -f docker-compose.dev.yml up -d
```

To launch specific containers, use:

```bash
docker compose -f docker-compose.dev.yml <service1-name> <service2-name> up -d
```

To stop the environment, run:

```bash
docker-compose -f docker-compose.dev.yml down
```

---

**Note:**  
Do **not** attempt to launch `docker-compose.test.yml` or `docker-compose.prod.yml` locally, as they require additional configurations specific to their respective environments.
