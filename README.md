# Yahoo Finance FastAPI

This project provides a FastAPI-based API for fetching and caching financial data using the Yahoo Finance API. It leverages Redis for caching to improve data retrieval speed and reduce repeated calls to external APIs.

## Repository

[GitHub Repository](https://github.com/saleh-saspx/yahoo-finance-fastapi)

## Prerequisites

- **Docker** and **Docker Compose** should be installed on your system.

## Project Structure

- `Dockerfile`: Sets up the Docker environment for the FastAPI application.
- `docker-compose.yml`: Configures Docker Compose to manage services, including FastAPI (`web`) and Redis (`redis`).
- `requirements.txt`: Specifies required Python packages.
- `main.py`: Main file for the FastAPI application.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/saleh-saspx/yahoo-finance-fastapi.git
cd yahoo-finance-fastapi
```

### 2. Build and Run the Containers

Use Docker Compose to build and start the containers:

```bash
docker-compose up --build
```

This command will:
- Build the Docker image for the FastAPI application.
- Start the FastAPI app on port `8011` and Redis on port `6371`.

### 3. Test the API

Once the containers are running, you can access the API at `http://localhost:8011`.

To check the server status, you can send a GET request to the root endpoint:

```bash
curl http://localhost:8011/
```

To explore available endpoints, open `http://localhost:8011/docs` in your browser. FastAPI provides an interactive Swagger UI for easy API testing and documentation.

### Example Endpoints

- **Crypto Prices**: `/yahoo/crypto`
- **Stock Prices**: `/yahoo/stock`
- **Country Currency Rates**: `/yahoo/country`
- **Oil Prices**: `/yahoo/oil`

### 4. Stop the Containers

To stop the running containers, use:

```bash
docker-compose down
```

This command stops and removes the containers but keeps the Docker images for faster restarts.

## Additional Information

- **Caching**: Redis is used to cache API responses for faster data retrieval.
- **Configuration**: Environment variables for Redis URL and other settings can be customized as needed.

