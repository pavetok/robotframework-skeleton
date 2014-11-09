# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fabric.api import local


def deploy(stand_name):
    local("cp stands/{0}/* .".format(stand_name))
    local("fig up")