# -*- coding: utf-8 -*-
from os.path import join, abspath, dirname


HOST_REPO_DIR = abspath(join(dirname(__file__), "..", ".."))
HOST_ROBOT_DIR = join(HOST_REPO_DIR, "robotframework-skeleton")
HOST_FAIL_DIR = join(HOST_ROBOT_DIR, "fails")
HOST_FAB_DIR = join(HOST_ROBOT_DIR, "fabfile")
HOST_LIB_DIR = join(HOST_ROBOT_DIR, "libraries")
HOST_RES_DIR = join(HOST_ROBOT_DIR, "resources")
HOST_TESTS_DIR = join(HOST_ROBOT_DIR, "tests")
LIB_MODULES_NAMES = ["actors", "components", "services", "pages"]
HOST_SRC_DIRS = [HOST_FAB_DIR, HOST_LIB_DIR, HOST_RES_DIR] + \
                [join(HOST_LIB_DIR, module_name) for module_name in LIB_MODULES_NAMES]

GUEST_REPO_DIR = "/repo"
GUEST_ROBOT_DIR = GUEST_REPO_DIR
GUEST_FAIL_DIR = join(GUEST_REPO_DIR, "fails")

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

STAND = {
    "app": {
        "name": "robotframeworkskeleton_app_1",
        "host": "hostname",
        "ip": None
    },
    "storage": {
        "name": None,
        "host": None,
        "ip": None
    }
}

APP_LOG_FILE = "/opt/tomcat/logs/catalina.2014-11-23.log"


if __name__ == "__main__":
    pass