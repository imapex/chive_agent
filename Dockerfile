FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"


RUN apk update && apk add --no-cache --virtual \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

# RUN pip install --upgrade pip

ADD ./app
WORKDIR /app
RUN pip install --requirement ./requirements/txt



CMD [ "python", "./agents/chive_agent_aci.py" ]