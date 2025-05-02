FROM python:3.12.9 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt

FROM python:3.12.9-slim
WORKDIR /app

COPY --from=builder /app/.venv .venv/
COPY . .

ENV FLASK_APP=app.py  # Altere para main.py se necessário

CMD ["/app/.venv/bin/gunicorn", "-b", "0.0.0.0:8080", "run:app"]
