#!/usr/bin/python3
""" genereate tgz archive """


from fabric.api import *
from datetime import datetime


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
