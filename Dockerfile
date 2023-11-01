FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install --no-install-recommends --yes curl

WORKDIR /api

COPY ./pyproject.toml ./poetry.lock ./

ARG PIP_VERSION=23.3.1
RUN pip install "pip==${PIP_VERSION}"

ARG POETRY_VERSION=1.5.1
RUN pip install "poetry==${POETRY_VERSION}"

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --only main

COPY . .

ENTRYPOINT ["poetry", "run", "gunicorn", "main:app", "-w" , "5", "-b",  "0.0.0.0:8080",  "--reload"]

