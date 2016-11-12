FROM python:2.7-alpine
MAINTAINER Justin Barksdale "jusbarks@cisco.com"

# You can provide comments in Dockerfiles
# Install any needed packages for your application
# Update

RUN apk update && apk add \
    git \
    libmysqlclient-dev \
    python \
    python-pip \

 && rm -rf /var/lib/apt/lists/*

# Install app dependencies
RUN pip install --upgrade pip

# Copy requirements.txt into apprpriate location
ADD . /app
RUN pip install --requirement ./app/requirements.txt


# Run BASH script
RUN chmod +x /app/chive_agent.sh
CMD ["/app/chive_agent.sh"]