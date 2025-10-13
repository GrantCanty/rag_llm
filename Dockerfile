# Start from a small Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to start the app
CMD ["python3", "backend/main.py"]
