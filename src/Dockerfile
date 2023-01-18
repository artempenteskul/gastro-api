FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.2

EXPOSE 8000

RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app/

COPY ../poetry.lock ../pyproject.toml /app/

RUN poetry config.virtualenvs.create false && poetry install --no-iteraction --no-ansi

COPY . /app/
