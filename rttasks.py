#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import env, hosts, roles, run
import requests
import os

@hosts(os.environ.get('SCHEDULER_URL'))
@roles('OOPP')
def ff():
    requests.get('http://plurkii.appspot.com/')
