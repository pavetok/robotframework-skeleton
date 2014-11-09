FROM malderhout/tomcat
MAINTAINER Pavel Vetokhin

RUN yum -y install epel-release
RUN yum -y install \
    python-pip \
    && yum clean all

COPY . /reqs
WORKDIR /reqs

RUN pip install -r guest-requirements.txt

# your code here