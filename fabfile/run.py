# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from fabric.api import task, local

from variables import HOST_ROBOT_DIR, HOST_FAB_DIR, HOST_LIBS_DIR, HOST_RES_DIR


@task
def test(name):
    pybot(test_name=name)


@task
def suite(name="tests"):
    pybot(suite_name=name)


@task
def all():
    pybot()


@task
def failed():
    pass


def pybot(test_name="*", suite_name="*"):
    PYTHONPATH = ":".join([HOST_FAB_DIR, HOST_LIBS_DIR, HOST_RES_DIR])
    local("pybot"
          " --outputdir {robot_dir}/output"
          " --debugfile debug.log"
          " --log log.html"
          " --report report.html"
          " --output output.xml"
          " --xunit xunit.xml"
          " --randomize all"
          " --removekeywords WUKS"
          " --pythonpath {pythonpath}"
          " --NoStatusRC"
          " --test '{test_name}'"
          " --suite '{suite_name}'"
          " '{robot_dir}/tests'"
          .format(robot_dir=HOST_ROBOT_DIR,
                  test_name=test_name,
                  pythonpath=PYTHONPATH,
                  suite_name=suite_name))