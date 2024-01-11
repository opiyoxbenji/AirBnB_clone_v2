#!/usr/bin/python3
"""
deletes out-of-date archives, using the function do_clean:
"""
from fabric.api import env, run, local, lcd
import os


env.hosts = ['54.162.75.3', '100.25.45.16']


def do_clean(number=0):
    """
    deletes archives
    """
    if number == 0 or number == 1:
        number = 1
    with cd.local("./versions"):
        local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
                xargs -d '\n' rm".format(1 + number))
    with cd("/data/web_static/releases"):
        run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
                xargs -d '\n' rm".format(1 + number))
