#!/usr/bin/env python
from fabric.api import run
from fabric.context_managers import env
from fabric.context_managers import cd
env.hosts = ['172.20.3.5','172.20.3.6','172.20.3.7']
env.user = 'root'
env.password = 'cds-china'
env.parallel = True

def init_tasker():
    run("export LC_ALL='en_US.UTF-8'; cd trunk; svn update")
