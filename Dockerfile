FROM python:3.11-slim

WORKDIR /app


# Copy the required files into the container
COPY requirements.txt requirements.txt
COPY app app
COPY run.py run.py

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose Flask API port
EXPOSE 5000

# Define launch command
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]