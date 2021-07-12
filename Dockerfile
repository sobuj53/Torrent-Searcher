FROM amd64/alpine:latest

WORKDIR /BOT

RUN chmod -R 777 /BOT

RUN apk add --no-cache --virtual .build-deps g++ libffi-dev openssl-dev python3-dev
RUN apk add --no-cache --update python3 py3-pip

RUN pip3 install --no-cache --upgrade pip wheel setuptools
#fake line
