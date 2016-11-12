FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"


RUN apk update && apk add --no-cache --virtual \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app
ADD ./agents /app/agents



CMD [ "python", "./agents/chive_agent_aci.py" ]