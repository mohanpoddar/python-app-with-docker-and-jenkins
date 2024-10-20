# Stage 1: Build
FROM python:3.12 AS builder

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Production
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY . .

# Set the entry point
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
