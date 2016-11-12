FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
# COPY chive_agent.sh chive_agent.sh
COPY chive_agent_aci.py chive_agent_aci.py

RUN apk update && apk add --no-cache --virtual \
#    bash \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

# Run BASH script
# RUN ["chmod", "+x",  "/chive_agent.sh"]
CMD ["python", "chive_agent_aci.py"]