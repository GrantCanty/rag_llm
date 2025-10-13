# Start from a small Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements into container
COPY requirements.txt .

#RUN git clone https://github.com/streamlit/streamlit-example.git .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8501

RUN ls

# Command to start the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
