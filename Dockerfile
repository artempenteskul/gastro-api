FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.2

WORKDIR /app

RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

#RUN pip3 install --upgrade pip
#RUN pip install "poetry==$POETRY_VERSION"

RUN pip3 install --upgrade pip

COPY ../requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ../src .

#RUN pip3 install -r requirements.txt

#COPY ../poetry.lock ../pyproject.toml /app/

#RUN POETRY_VIRTUALENVS_CREATE=false && poetry install --no-ansi

#COPY . .

#RUN poetry install


CMD ["python3", "manage.py", "runserver"]
