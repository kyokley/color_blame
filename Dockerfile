FROM python:2.7-alpine

RUN apk add --no-cache git

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app
RUN pip install .
