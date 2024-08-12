FROM python:3.12
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV POETRY_VIRTUALENVS_CREATE=false
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  && pip install "poetry==1.8.2"

# set work directory
WORKDIR /src
COPY pyproject.toml poetry.lock /src/

# Install dependencies:
RUN poetry install --only main --no-interaction
COPY . .
