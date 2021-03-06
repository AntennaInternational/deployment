from  __future__ import with_statement
from fabric.api import *

from contextlib import contextmanager as _ctxmgr
@_ctxmgr
def virtualenv():
    with lcd(os.path.join(venv_dir, app_name)):
        with prefix('. bin/activate'):
            yield
import os

scripts_dir = os.path.join(os.path.dirname(__file__), 'sh')
supervisor_dir = os.path.join(os.path.dirname(__file__), 'supervisor')
target_dir = '/webapps'
venv_dir = '/webapps/venvs/'
app_name = 'rack_server'
repo_url = "https://github.com/AntennaInternational/rack-server.git"
requirements_file = 'requirements.txt'




def pull_git(origin='master'):
    with lcd(target_dir):
        local('sudo rm -f -R {}'.format(app_name))
        local('mkdir -p {}'.format(app_name))
        local('git clone {0} {1}'.format(repo_url, os.path.join(target_dir, app_name)))
    '''
    with lcd(os.path.join(target_dir,app_name)):
        local('ls')
        local('git pull origin {}'.format(origin))
    '''
def create_venv():
    local('mkdir -p {}'.format(venv_dir))
    with lcd(venv_dir):
        cd(venv_dir)
        local('virtualenv {}'.format(app_name))
        with lcd(app_name):
            local('mkdir -p logs')


def install_pip_requirements():
    rfile = os.path.join(target_dir, app_name, requirements_file)
    with virtualenv():
        local('pip install -r {}'.format(rfile))

def install_supervisor_configs():
    supervisor_conf_dir = '/etc/supervisor/conf.d'
    print 'SUPERVISOR DIR {}'.format(supervisor_dir)
    with lcd(supervisor_dir):
        local('cp * {}'.format(supervisor_conf_dir))

def install_startup_scripts():
    venv = os.path.join(venv_dir, app_name, 'bin')
    script_files = os.listdir(scripts_dir)
    with lcd(scripts_dir):

        local('cp * {}'.format(venv))
    with lcd(venv):
        for f in script_files:
            local('chmod +x ./{}'.format(f))

if __name__ == '__main__':
    pull_git()
    create_venv()

    install_supervisor_configs()
    install_startup_scripts()
    install_pip_requirements()