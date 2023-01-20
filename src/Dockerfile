FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.2

WORKDIR /app

RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

RUN pip3 install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

COPY ../poetry.lock /app
COPY ../pyproject.toml /app

RUN poetry config.virtualenvs.create false && poetry install --no-iteraction --no-ansi

COPY . .

CMD ["python3", "manage.py", "runserver"]
