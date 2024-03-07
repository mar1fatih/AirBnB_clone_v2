#!/usr/bin/python3
""" distributes an archive to the web servers """
from os import path
from fabric.api import put, run, env

env.host = [35.174.184.183, 54.237.227.74]


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if path.exists(archive_path) is False:
        return False
    _file = archive_path.split('/')[-1]
    file_ = _file.split(".")[0]
    _path = "/data/web_static/releases/"
    put(archive_path, '/tmp/')
    run('mkdir -p {}{}/'.format(_path, file_))
    run('tar -xzf /tmp/{} -C {}{}/'.format(_file, _path, file_))
    run('rm /tmp/{}'.format(_file))
    run('mv {}{}/web_static/* {}{}/'.format(_path, file_, _path, file_))
    run('rm -rf {}{}/web_static'.format(_path, file_))
    run('rm -rf /data/web_static/current')
    run('ln -s {}{}/ /data/web_static/current'.format(_path, file_))
    return True
