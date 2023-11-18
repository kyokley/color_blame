ARG BASE_IMAGE=python:3.11-alpine

FROM ${BASE_IMAGE} AS builder

ENV POETRY_VENV=/poetry_venv
RUN python3 -m venv $POETRY_VENV

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -U pip wheel

RUN apk add --no-cache git g++ libffi-dev

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN $POETRY_VENV/bin/pip install --upgrade pip poetry && $POETRY_VENV/bin/poetry install --no-dev

FROM ${BASE_IMAGE} AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VENV=/poetry_venv

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk add --no-cache git g++ libffi-dev

COPY --from=builder ${POETRY_VENV} ${POETRY_VENV}
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

FROM base AS dev
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY poetry.lock pyproject.toml /app/
RUN $POETRY_VENV/bin/pip install --upgrade pip poetry && \
        $POETRY_VENV/bin/poetry install

FROM base AS prod
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /app
RUN $POETRY_VENV/bin/poetry build && $POETRY_VENV/bin/poetry install --no-dev
