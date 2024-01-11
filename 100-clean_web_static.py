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
    if number == 0 or number == 1:
        number = 1
    arch = sorted(os.listdir("versions"))
    [archs.pop() for num in range(number)]
    with lcd("versions"):
        for dels in arch:
            local("rm ./{}".format(dels))
    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [dels for dels in arch if "web_static_" in dels]
        [arch.pop() for num in range(number)]
        [run("rm -rf ./{}".format(dels)) for dels in arch]
