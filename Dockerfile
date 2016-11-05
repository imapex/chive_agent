# VERSION 1.0
FROM python:2-alpine
MAINTAINER Justin Barksdale, "jusbarks@cisco.com"


RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip \

 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone https://github.com/datacenter/acitoolkit
WORKDIR acitoolkit
RUN python setup.py install
