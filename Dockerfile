FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1

RUN apk update && \
   apk add --no-cache mariadb-connector-c-dev mariadb-dev && \
   apk add --no-cache --virtual .build-deps build-base mariadb-connector-c-dev && \
   pip install mysqlclient==2.0.3 && \
   apk del .build-deps

RUN apk add --no-cache phpmyadmin

RUN mkdir /proyecto

WORKDIR /proyecto/

COPY requirements.txt /proyecto/

RUN python -m pip install -r requirements.txt && \
    apk add --no-cache mariadb-connector-c-dev && \
    pip install mysqlclient==2.0.3 && \
    apk del .build-deps

COPY . /proyecto/

CMD ["node-red"]
