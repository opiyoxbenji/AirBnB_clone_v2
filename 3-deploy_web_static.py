#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function deploy:
"""
from fabric.api import env, local, run, put
from datetime import datetime
from os.path import isfile, exists
from os import path
import os


env.hosts = ['54.162.75.3', '100.25.45.16']


def do_pack():
    """
    distributes an archive to your web servers, using the function deploy
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


def do_deploy(archive_path):
    """
    send archive to web servers
    """
    if not isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_file = archive_path.split('/')[-1]
        extension = archive_file.split(".")[0]
        path_et = "/data/web_static/releases/{}/".format(extension)
        run("mkdir -p {}".format(path_et))
        run("tar -xzf /tmp/{} -C {}".format(
            archive_file, path_et))
        run("rm /tmp/{}".format(archive_path))
        run("mv {}/web_static/* {}".format(path_et, path_et))
        run("rm -rf {}web_static".format(path_et))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_file))
        return True
    except Exception as e:
        return False


def deploy():
    """
    deplouy web_static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
