# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fabric.api import local


def deploy(stand_name):
    local("cp stands/{0}/Dockerfile .".format(stand_name))
    local("cp stands/{0}/.dockerignore .".format(stand_name))
    local("ansible-playbook ansible/playbook.yml")
    # local("fig up")