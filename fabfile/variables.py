# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import join, abspath, dirname


HOST_REPO_DIR = abspath(join(dirname(__file__), "..", ".."))
HOST_ROBOT_DIR = join(HOST_REPO_DIR, "robotframework-skeleton")
HOST_FAB_DIR = join(HOST_ROBOT_DIR, "fabfile")
HOST_LIBS_DIR = join(HOST_ROBOT_DIR, "libraries")
HOST_RES_DIR = join(HOST_ROBOT_DIR, "resources")
HOST_TESTS_DIR = join(HOST_ROBOT_DIR, "tests")


if __name__ == "__main__":
    pass