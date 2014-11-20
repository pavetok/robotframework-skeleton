# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from robot.api import logger


class BaseLibrary(object):

    @property
    def logger(self):
        if hasattr(self, "__logger"):
            return self.__logger
        else:
            self.__logger = logger
        return self.__logger
