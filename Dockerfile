FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary

CMD ["uvicorn", "src.reservas.api:app", "--host", "0.0.0.0", "--port", "8000"]