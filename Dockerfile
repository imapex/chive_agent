FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

RUN apk update && apk add --no-cache --virtual \
#    git \
#    libmysqlclient-dev \
#    python \
#    python-pip \
#  && rm -rf /var/cache/apk/* \

ADD . /app
WORKDIR /app

RUN pip install -r /requirements.txt

CMD [ "python", "./agents/chive_agent_aci.py" ]