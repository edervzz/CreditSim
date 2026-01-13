FROM python:3.11-slim

WORKDIR /app

ENV POETRY_VERSION=2.2.1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* README.md ./
COPY src ./src

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["gunicorn", "backend.main:app", "-c", "gunicorn.conf.py"]
