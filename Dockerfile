FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential git curl \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install extra package manager
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN ln -sf /root/.poetry/bin/poetry /usr/local/bin/poetry
ENV POETRY_VIRTUALENVS_CREATE=false

RUN mkdir -p /app
WORKDIR /app

# install dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

# set entrypoint
COPY docker-entrypoint.sh /entrypoint
ENTRYPOINT ["/entrypoint"]

# copy code & tests
COPY manage.py pytest.ini /app/
COPY src /app/src
COPY tests /app/tests
