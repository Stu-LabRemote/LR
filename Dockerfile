FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev mariadb-dev build-base libffi-dev openssl-dev mysql-client && \
    pip install mysqlclient==2.0.3 && \
    apk del mariadb-connector-c-dev mariadb-dev build-base libffi-dev openssl-dev mysql-client

# Instalar las herramientas de compilación
RUN apk add --no-cache build-base

RUN apk add --no-cache phpmyadmin

RUN apk add --no-cache libffi-dev

RUN apk add --no-cache linux-headers

RUN mkdir /proyecto
WORKDIR /proyecto/

COPY requirements.txt /proyecto/
RUN python -m pip install -r requirements.txt

RUN apk add --no-cache mariadb-connector-c-dev mariadb-dev build-base libffi-dev openssl-dev mysql-client

COPY . /proyecto/

CMD ["node-red"]
