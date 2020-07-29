ARG BASE_IMAGE=python:3.7-alpine


FROM ${BASE_IMAGE} AS builder
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PATH="$PATH:/root/.poetry/bin"

RUN apk update && apk add --no-cache curl git

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock

RUN pip install pip --upgrade && \
    /root/.poetry/bin/poetry install --no-dev && \
    pip install git+https://github.com/kyokley/terminaltables.git

FROM ${BASE_IMAGE} AS base
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PATH="$PATH:/root/.poetry/bin"

RUN apk update && apk add --no-cache curl

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY --from=builder /venv /venv

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock

FROM base AS final
COPY . /app
RUN python setup.py install


FROM base AS dev
RUN apk add --no-cache gcc
RUN pip install pip --upgrade && \
    /root/.poetry/bin/poetry install
COPY . /app
RUN python setup.py develop
