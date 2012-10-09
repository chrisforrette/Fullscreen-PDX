from __future__ import with_statement
import datetime
import os
from fabric.api import *
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project

env.local_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'html') + '/'

RSYNC_EXCLUDES = (
    '.DS_Store',
    '*.pyc',
    '.svn',
    '.git*',
    '.sass*',
    'settings_local.py',
    'uploads',
    'fabfile.py',
    '*.log',
)

def dev():
    env.user = 'root'
    env.hosts = ['ve.znsm8v5x.vesrv.com']
    env.remote_path = '/home/static.chrisforrette.com'

def push():

    """
    Backup database, push code, and restart server. This must be preceded by a setup command call, e.g.:

        fab dev push

    """

    require('remote_path', provided_by=('dev',))

    rsync_project(
        local_dir=env.local_path,
        remote_dir=env.remote_path,
        exclude=RSYNC_EXCLUDES
    )

    run('service nginx restart')