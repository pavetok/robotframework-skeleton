# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.api import task, local


@task
def deploy(stand_name):
    local("/bin/cp -p stands/{0}/* .".format(stand_name))
    # local("fig build")
    local("fig up")