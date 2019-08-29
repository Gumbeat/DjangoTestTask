FROM python:3.7

ENV APP_ROOT /test_task
RUN mkdir /test_task

RUN apt-get update

WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000 && python manage.py makemigrations && python manage.py migrate
# docker run -d --network=host