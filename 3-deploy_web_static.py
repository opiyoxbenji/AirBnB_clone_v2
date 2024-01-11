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
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_file = archive_path.split('/')[-1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/".format(archive_file))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_path.split('/')[-1], archive_file))
        run("rm /tmp/{}".format(archive_path.split('/')[-1]))
        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
                    archive_file, archive_file))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(archive_file))
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
