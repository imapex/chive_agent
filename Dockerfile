FROM alpine:latest
MAINTAINER Your Name climann2@cisco.com

# You can provide comments in Dockerfiles
# Install any needed packages for your application
# Update
RUN apk add --update python py-pip

RUN apt-get update && apt-get install -y \
    git \
    python\
    python-pip\
 && rm -rf /var/lib/apt/lists/*

# Install app dependencies
RUN pip install --upgrade pip


#COPY requirements.txt /tmp/
ADD . /app
WORKDIR /app
RUN pip install --requirement ./requirements.txt

#COPY . /tmp/

# Run python program

CMD ["python", "./chive_agent_api.py"]