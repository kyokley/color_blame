ARG BASE_IMAGE=python:3.10-alpine

FROM ${BASE_IMAGE} AS builder

RUN pip install -U pip wheel

ENV POETRY_VENV=/poetry_venv
RUN python3 -m venv $POETRY_VENV

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN apk add --no-cache git g++ libffi-dev

COPY poetry.lock pyproject.toml /app/

RUN $POETRY_VENV/bin/pip install poetry && $POETRY_VENV/bin/poetry install --no-dev

FROM ${BASE_IMAGE} AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VENV=/poetry_venv

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=builder ${POETRY_VENV} ${POETRY_VENV}
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

RUN apk add --no-cache git g++ libffi-dev

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install -U pip wheel

COPY . /app
RUN $POETRY_VENV/bin/pip install poetry && \
        $POETRY_VENV/bin/poetry install

FROM base AS dev
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN $POETRY_VENV/bin/pip install poetry && \
        $POETRY_VENV/bin/poetry install && \
        python setup.py develop

FROM base AS prod
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python setup.py install
