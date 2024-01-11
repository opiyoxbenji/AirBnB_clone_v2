#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import env, put, run, local
import os


env.hosts = ['54.162.75.3', '100.25.45.16']


def do_deploy(archive_path):
    """
    sends archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_file = os.path.basename(archive_path)
        release_folder = "/data/web_static/releases/{}/".format(
                archive_file[:4]
        )
        put(archive_path, '/tmp/')
        run("rm -rf {}".format(release_folder))
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_file, release_folder))
        run("rm /tmp/{}".format(archive_file))
        run("mv {}/web_static/* {}".format(release_folder, release_folder))
        run("rm -rf {}web_static".format(release_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
