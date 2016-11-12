FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

# You can provide comments in Dockerfiles
# Install any needed packages for your application
# Update

#RUN apk update && apk add \
#    git \
#   libmysqlclient-dev \
#    python \
#    python-pip \

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
COPY chive_agent.sh chive_agent.sh
COPY agent.py agent.py

RUN apk update && apk add --no-cache --virtual \
    bash \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

# Run BASH script
RUN ["chmod", "+x",  "/chive_agent.sh"]
CMD ["./chive_agent.sh"]