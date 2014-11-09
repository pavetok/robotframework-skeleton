FROM malderhout/tomcat

RUN yum -y install epel-release
RUN yum -y install \
    python-pip \
    && yum clean all

COPY . /build
WORKDIR /build

RUN pip install -r requirements/guest-reqs.txt

# your code here