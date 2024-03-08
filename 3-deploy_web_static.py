#!/usr/bin/python3
""" Full deployment """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['35.174.184.183', '54.237.227.74']


def do_pack():
    """ make an archive on web_static """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if path.exists(archive_path) is False:
        return False
    try:
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
    except:
        return False


def deploy():
    """ Creates and distributes an archive to the web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
