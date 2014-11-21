# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.api import task, local

from variables import HOST_ROBOT_DIR, BASE_ROBOT_ARGS, ROOT_SUITE_NAME


@task
def test(name):
    run_robot(test=name)


@task
def suite(name):
    run_robot(suite=name)


@task
def tags(*tags):
    run_robot(tags="AND".join(tags))


@task
def all():
    run_robot()


@task
def failed():
    pass


def run_robot(test="*", suite=ROOT_SUITE_NAME, tags="*"):
    local("pybot " + " ".join(
        BASE_ROBOT_ARGS + [
            "--include", "'{0}'".format(tags),
            "--test", "'{0}'".format(test),
            "--suite", "'{0}'".format(suite),
            "{0}/tests".format(HOST_ROBOT_DIR)
        ]))