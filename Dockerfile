FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt upgrade \
    && apt install postgresql gcc python3-dev musl-dev -y

WORKDIR /mysite
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./mysite /mysite
