ARG BASE_IMAGE=python:3.10-alpine

FROM ${BASE_IMAGE} AS base

RUN apk add --no-cache git g++ libffi-dev

COPY requirements.txt /app/requirements.txt
RUN pip install -U pip && pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app
RUN pip install .

FROM base AS dev
RUN pip install -r /app/dev_requirements.txt
