FROM python:3.11-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG PG_DB
ARG PG_HOST
ARG PG_USER
ARG PG_PW
ARG REPO
ENV PG_DB ${PG_DB}
ENV PG_HOST ${PG_HOST}
ENV PG_USER ${PG_USER}
ENV PG_PW ${PG_PW}
ENV REPO ${REPO}

RUN apt-get update && apt-get install -y build-essential libffi-dev

COPY ./requirements.txt requirements.txt

RUN pip install types-Pygments types-colorama types-setuptools types-ujson
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

COPY . .

RUN pip install notebook
RUN cd ./notebooks
RUN python -m notebook
RUN cd ..

CMD python etl.py