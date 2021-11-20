FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api
COPY . /api

RUN pip install --upgrade pip
RUN pip install -r requirement

CMD [ "gunicorn", "--bind", ":8000", "project_api.wsgi:application"]