FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Some apps use wsgi:app, others use manage:app. We'll use python wsgi.py as fallback if it exists, or gunicorn.
CMD ["python", "wsgi.py"]
