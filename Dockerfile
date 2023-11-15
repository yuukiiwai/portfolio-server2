FROM python:3.11.4-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN apt-get update -y
RUN apt-get -y install gcc
ADD ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
