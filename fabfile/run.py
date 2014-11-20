# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.api import task
from robot.run import run as run_robot

from variables import HOST_ROBOT_DIR, HOST_SRC_DIRS


@task
def test(name):
    pybot(test_name=name)


@task
def suite(name):
    pybot(suite_name=name)


@task
def all():
    pybot()


@task
def failed():
    pass


def pybot(test_name="*", suite_name="*"):
    run_robot("{0}/tests".format(HOST_ROBOT_DIR),
        outputdir="{0}/output".format(HOST_ROBOT_DIR),
        debugfile="debug.log",
        log="log.html",
        report="report.html",
        output="output.xml",
        xunit="xunit.xml",
        randomize="all",
        removekeywords="WUKS",
        pythonpath=":".join(HOST_SRC_DIRS),
        NoStatusRC=True,
        test=test_name,
        suite=suite_name)


if __name__ == "__main__":
    import sys
    test(" ".join(sys.argv[1:]))