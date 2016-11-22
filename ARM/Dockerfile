FROM alpine:3.4
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade-pip setuptools && \
    rm -r /root/.cache

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./agents/chive_agent_aci.py" ]