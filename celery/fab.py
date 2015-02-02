from  __future__ import with_statement
from fabric.api import *

from contextlib import contextmanager as _ctxmgr
import os

scripts_dir = os.path.join(os.path.dirname(__file__), 'sh')
supervisor_dir = os.path.join(os.path.dirname(__file__), 'supervisor')
venv_dir = '/webapps/venvs/rack_webapp'


@_ctxmgr
def virtualenv():
    with lcd(venv_dir):
        with prefix('source bin/activate'):
            yield

def install_startup_scripts():
    bin_dir = os.path.join(venv_dir, 'bin')
    script_files = os.list_dir(scripts_dir)
    with lcd(scripts_dir):
        local('chmod +x *')
        local('mv * {}'.format(bin_dir))
    with lcd(venv):
        for f in script_files:
            local('chmod +x ./{}'.format(f))

def install_supervisor_configs():
    supervisor_conf_dir = '/etc/supervisor/conf.d'
    with lcd(supervisor_dir):
        local('cp * {}'.format(supervisor_conf_dir))

if __name__ == '__main__':
    install_supervisor_configs()
    install_startup_scripts()