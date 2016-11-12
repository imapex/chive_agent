FROM python:2.7-slim
MAINTAINER Your Name climann2@cisco.com

# You can provide comments in Dockerfiles
# Install any needed packages for your application
# Update

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip \
    libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*

# Install app dependencies
RUN pip install --upgrade pip

#COPY requirements.txt /tmp/
ADD . /app
#WORKDIR /app
RUN pip install --requirement ./app/requirements.txt

#COPY . /tmp/

# Run python program

#CMD ["python", "./chive_agent_aci.py"]

# Run BASH script
RUN chmod +x /app/chive_agent.sh
CMD ["/app/chive_agent.sh"]