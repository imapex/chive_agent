FROM hypriot/rpi-alpine-scratch
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

RUN apk add --update \
    python \
    py-pip \

  && rm -rf /var/cache/apk/*

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./agents/chive_agent_aci.py" ]