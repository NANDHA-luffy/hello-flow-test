# Use the official lightweight FastAPI image with Uvicorn/Gunicorn
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app ./app

# The base image's default command runs:
# gunicorn -k uvicorn.workers.UvicornWorker app.main:app