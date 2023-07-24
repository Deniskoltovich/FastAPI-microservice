FROM python:3.10.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
COPY scripts/entrypoint.sh .
COPY scripts/entrypoint_beat.sh .
COPY scripts/entrypoint_celery.sh .

RUN chmod +x ./entrypoint.sh ./entrypoint_beat.sh ./entrypoint_celery.sh


RUN pipenv install --system
COPY . /code
