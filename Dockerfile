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

RUN apk update && apk add --no-cache --virtual .build-deps \
        git \
        libmysqlclient-dev \
        python \
        python-pip \
        && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \

    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

COPY . .

# Run BASH script
RUN chmod +x /app/chive_agent.sh
CMD ["/app/chive_agent.sh"]