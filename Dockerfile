FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.2
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /app

RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

RUN pip3 install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"

#COPY requirements.txt .
#RUN pip3 install -r requirements.txt --no-cache-dir

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .
