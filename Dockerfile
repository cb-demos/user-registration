FROM python:3.9-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv

RUN pipenv install --system --deploy

COPY . /app/


CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]