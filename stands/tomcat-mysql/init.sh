#!/bin/bash

/usr/sbin/sshd -D &
/opt/tomcat/bin/catalina.sh run
