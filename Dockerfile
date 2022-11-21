FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip3 install .

CMD subreddit-to-apprise
