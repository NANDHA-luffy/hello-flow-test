# Tiny FastAPI Hello Service

A minimal FastAPI application that returns a greeting at the root endpoint and provides a simple health‑check endpoint.

## Endpoints

| Method | Path    | Query   | Description                               |
|--------|---------|---------|-------------------------------------------|
| GET    | `/`     | `msg`   | Returns `{"greeting": "<msg>"}`. If `msg` is omitted, returns `{"greeting": "Hello, World!"}`. |
| GET    | `/health`| –       | Returns `{"status": "ok"}` – useful for liveness probes. |

## Running Locally
