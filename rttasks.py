#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import env, hosts, roles, run
import os

@hosts(os.environ.get('SCHEDULER_URL'))
@roles('OOPP')
def ff():
    run('python ./rttasks1.py')

ff()