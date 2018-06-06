FROM python:2.7-slim

MAINTAINER SayfEddine

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/doitnow/manage.py", "runserver", "0.0.0.0"]
