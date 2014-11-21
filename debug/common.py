# -*- coding: utf-8 -*-
from robot.run import run_cli

from variables import HOST_ROBOT_DIR, BASE_ROBOT_ARGS, ROOT_SUITE_NAME


def run_robot(test="*", suite=None):
    run_cli(BASE_ROBOT_ARGS + [
        "--test", "{0}".format(test),
        "--suite", "{0}".format(suite if suite else ROOT_SUITE_NAME),
        "{0}/tests".format(HOST_ROBOT_DIR)
    ])