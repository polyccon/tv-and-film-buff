ARG DOCKER_IMAGE_BASE=python:3.8.10-slim
FROM ${DOCKER_IMAGE_BASE} as base_python

# Virtualenv setup ------------------------------------------------------------

FROM base_python as venv

RUN \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    zlib1g-dev \
    autoconf \
    automake \
    make \
    gcc \
    perl \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    && \
    pip install --no-cache-dir virtualenv==20.0.18 setuptools==44.1.0 &&\
    true

RUN virtualenv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --no-binary psycopg2

# Main container --------------------------------------------------------------

FROM base_python as base

RUN \
    apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev libcurl4-openssl-dev openssl&&\
    true

# Copy python packages
COPY --from=venv /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV LOG_LEVEL=DEBUG
ENV DJANGO_SETTINGS_MODULE=tv_and_film_buffAPI.config.settings
ENV PYTHONUNBUFFERED=1

EXPOSE 5500