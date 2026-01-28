# 1. Use lightweight Python image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY . .

# 5. Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]