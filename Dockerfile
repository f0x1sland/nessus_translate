# test version
FROM python:3.8.13-slim-buster

WORKDIR /usr/src/nest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

COPY ./requirements.txt /usr/src/nest/requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD [ "python", "run.py" ]