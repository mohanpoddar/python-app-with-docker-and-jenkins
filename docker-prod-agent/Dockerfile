# Use the official Jenkins agent image as the base
FROM jenkins/inbound-agent:latest

# Install Docker
USER root
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# RUN add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN sleep 5
RUN cat /etc/apt/sources.list.d/docker.list
RUN sleep 5
RUN apt-get update
RUN apt-get install -y docker-ce-cli docker-ce

# Configure Docker to run as non-root user
#RUN groupadd docker
RUN usermod -aG docker jenkins

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Enable DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker
