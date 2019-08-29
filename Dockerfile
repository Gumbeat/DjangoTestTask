FROM python:3.7

ENV APP_ROOT /test_task
RUN mkdir /test_task

RUN apt-get update

# Create the log file to be able to run tail

# RUN touch /var/log/cron.log

WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
#VOLUME . ${APP_ROOT}
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000 && python manage.py makemigrations && python manage.py migrate

# docker run -d --network=host --mount type=bind,source="$(pwd)",target=/test_task