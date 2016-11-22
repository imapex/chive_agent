FROM hypriot/rpi-alpine-scratch
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

RUN apk update && \
    apk upgrade && \
    apk add python && \
    apk add python-pip && \
    rm -rf /var/cache/apk/*
ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./agents/chive_agent_aci.py" ]