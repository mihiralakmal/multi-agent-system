FROM python:3.11

WORKDIR /app

# Copy backend only
COPY backend ./backend
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix imports for clean architecture
ENV PYTHONPATH=/app

# Run FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]