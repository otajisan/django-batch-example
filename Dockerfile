FROM python:3.11-slim-bullseye

WORKDIR /django-batch-example
COPY . /django-batch-example

RUN apt update && \
    apt clean -y

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry install --no-dev

CMD ["poetry", "run", "./manage.py", "greet"]
