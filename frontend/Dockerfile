FROM python:3.11

# Set working directory INSIDE frontend
WORKDIR /app/frontend

# Copy only frontend code
COPY frontend/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 3000

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=3000", "--server.address=0.0.0.0"]