FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG PIP_VERSION=23.3.1
RUN pip install "pip==${PIP_VERSION}"

COPY ./requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

COPY ./memory_check.py ./

CMD ["python3", "memory_check.py"]

