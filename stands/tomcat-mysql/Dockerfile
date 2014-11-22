FROM malderhout/tomcat

# RUN yum -y update; yum clean all
RUN yum -y install epel-release && yum clean all
RUN yum -y install gcc && yum clean all

RUN yum -y install \
    openssh-server \
    python-devel \
    python-pip \
    && yum clean all

ENV HOME /root
COPY . /build
WORKDIR /build

RUN pip install -r requirements/guest-reqs.txt

RUN ssh-keygen -A
COPY id_rsa.pub /root/.ssh/authorized_keys

CMD /build/init.sh