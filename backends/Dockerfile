FROM python:3.11-alpine

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DJANGO_SETTINGS_MODULE=app.settings
ENV DockerHome='/home/app'


RUN pip install --upgrade pip
# RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev


COPY req.txt .
RUN pip install -r req.txt              

ARG CACHEBUST=1

COPY ./app/ ${DockerHome}


RUN chmod +x ${DockerHome}/api.sh

# RUN chmod +x ${DockerHome}/sockets.sh

WORKDIR ${DockerHome}