# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bases import BaseService


class EntityService(BaseService):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def new_entity(self, **kwargs):
        pass