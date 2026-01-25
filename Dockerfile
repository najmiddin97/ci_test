FROM jenkins/jenkins:lts-jdk21

USER root

# Python va pip o'rnatish
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Pre-installed venv va requirements
# Hozirki build context = ci_test
COPY requirements.txt /tmp/requirements.txt

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r /tmp/requirements.txt

USER jenkins
WORKDIR /var/jenkins_home

