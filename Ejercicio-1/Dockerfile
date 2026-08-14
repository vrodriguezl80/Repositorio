FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_PORT=8080

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

RUN useradd --create-home --shell /bin/bash testuser

COPY app.py .

RUN chown -R testuser:testuser /app

USER testuser

EXPOSE 8080

CMD ["python", "app.py"]