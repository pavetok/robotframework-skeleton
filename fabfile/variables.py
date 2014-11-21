# -*- coding: utf-8 -*-
from os.path import join, abspath, dirname


HOST_REPO_DIR = abspath(join(dirname(__file__), "..", ".."))
HOST_ROBOT_DIR = join(HOST_REPO_DIR, "robotframework-skeleton")
HOST_FAB_DIR = join(HOST_ROBOT_DIR, "fabfile")
HOST_LIB_DIR = join(HOST_ROBOT_DIR, "libraries")
HOST_RES_DIR = join(HOST_ROBOT_DIR, "resources")
HOST_TESTS_DIR = join(HOST_ROBOT_DIR, "tests")
LIB_MODULES_NAMES = ["actors", "subsystems", "services", "pages"]
HOST_SRC_DIRS = [HOST_FAB_DIR, HOST_LIB_DIR, HOST_RES_DIR] + \
                [join(HOST_LIB_DIR, module_name) for module_name in LIB_MODULES_NAMES]

ROOT_SUITE_NAME = "tests"
BASE_ROBOT_ARGS = [
    "--outputdir", "{0}/output".format(HOST_ROBOT_DIR),
    "--debugfile", "debug.log",
    "--log", "log.html",
    "--report", "report.html",
    "--output", "output.xml",
    "--xunit", "xunit.xml",
    "--randomize", "all",
    "--removekeywords", "WUKS",
    "--pythonpath", ":".join(HOST_SRC_DIRS),
    "--NoStatusRC"
]


if __name__ == "__main__":
    pass