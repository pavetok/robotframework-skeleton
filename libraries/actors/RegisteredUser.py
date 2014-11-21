# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bases import BaseUser


class RegisteredUser(BaseUser):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def login(self):
        self.logger.debug("User logged in")