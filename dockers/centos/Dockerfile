FROM centos:centos7
MAINTAINER Pavel Vetokhin

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install git; yum clean all
RUN yum -y install mysql-server mysql; yum clean all
RUN yum -y install python-pip; yum clean all

ADD . /repo

RUN cd /repo; pip install -r guest-requirements.txt

EXPOSE 3306 8080

CMD ["/bin/bash"]