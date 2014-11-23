FROM malderhout/tomcat

#RUN yum -y update; yum clean all
RUN yum -y install epel-release
RUN yum -y install gcc

RUN yum -y install \
    python-devel \
    python-pip \
    && yum clean all

ENV HOME /root
COPY . /build
WORKDIR /build

RUN pip install -r requirements/guest-reqs.txt