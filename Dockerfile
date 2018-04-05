FROM python:alpine

WORKDIR /bin/pto-slackbot/src/

RUN apk add --no-cache build-base gcc
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY pto-slackbot /bin/pto-slackbot
