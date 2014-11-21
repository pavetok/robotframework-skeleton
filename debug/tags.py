# -*- coding: utf-8 -*-
import sys
from common import run_robot

run_robot(tags="AND".join(sys.argv[1:]))