FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH
COPY requirements.txt /
COPY chive_agent_aci.py /

RUN apk update && apk add --no-cache --virtual \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

RUN pip install -r /app/requirements.txt

CMD [ "python", "./chive_agent_aci.py" ]