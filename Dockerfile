FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt install --no-install-recommends --yes curl


WORKDIR /api

COPY ./pyproject.toml ./poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --only main

COPY . .

ENTRYPOINT ["poetry", "run", "gunicorn", "main:app", "-w" , "5", "-b",  "0.0.0.0:8080",  "--reload"]

