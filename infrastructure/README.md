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

1. **Launch the development environment**:

   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

2. **Stop the environment** when you're done:

   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

---

**Note:**  
Do **not** attempt to launch `docker-compose.test.yml` or `docker-compose.prod.yml` locally, as they require additional configurations specific to their respective environments.
