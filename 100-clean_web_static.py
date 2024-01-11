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
    number = int(number)
    number += 1
    with lcd("versions"):
        local("ls -lt | tail -n +{} | xargs -I {{}} rm {{}}".format(number))
    releases = run("ls -lt /data/web_static/releases").split('\n')
    for release in releases:
        run ("rm -rf /data/web_static/releases/{}".format(release))
