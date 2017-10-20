# -- Dockerfile -- #
#
# docker build -t soe .
# docker run -dit --name soe-isntance -v `pwd`:/storage/app -p 25066:80 soe
# docker exec -it soe-instance /bin/bash

FROM ubuntu:16.04

LABEL Description="Attendance Container" Version="1.0"

# Install generic tools
RUN apt-get update && apt-get install -y \
  sudo \
  vim \
  net-tools \
  curl

# Add node source repository to install the latest version
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

# Preconfigure mysql client & server
RUN echo 'mysql-server mysql-server/root_password password testpwd' | debconf-set-selections
RUN echo 'mysql-server mysql-server/root_password_again password testpwd' | debconf-set-selections

# Install basic tools
RUN apt-get update && apt-get install -y \
  mysql-server \
  mysql-client \
  libmysqlclient-dev \
  python-pip \
  python-dev \
  nodejs

# Upgrade python
RUN pip install --upgrade pip

# Bring the process starter
COPY startup.sh /root/
RUN chmod +x /root/startup.sh

EXPOSE 5000 3306

ENTRYPOINT [ "/root/startup.sh" ]
