#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo
using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                now.year, now.month, now.day, now.hour, now.minute, now.second
        )
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
