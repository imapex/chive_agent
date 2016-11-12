FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"


RUN apk add -U \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir \
          setuptools \
          wheel

# RUN pip install --upgrade pip

ADD . /app
WORKDIR /app
RUN pip install --requirement ./requirements.txt



CMD [ "python", "./agents/chive_agent_aci.py" ]