FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH
COPY requirements.txt requirements.txt


RUN apk update && apk add --no-cache --virtual \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

RUN pip install -r /requirements.txt

ADD . /agents

CMD [ "python", "./agents/chive_agent_aci.py" ]