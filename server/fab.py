__author__ = 'brendan'
from fabric.api import local, cd, lcd,settings
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
    with lcd(os.path.join(target_dir,app_name)):
        local('ls')
        local('git pull origin {}'.format(origin))

def create_venv():
    local('mkdir -p {}'.format(venv_dir))
    with lcd(venv_dir):
        cd(venv_dir)
        local('virtualenv {}'.format(app_name))

def install_pip_requirements():
    rfile = os.path.join(target_dir, app_name, requirements_file)
    local('source {}'.format(os.path.join(venv_dir, app_name, 'bin', 'activate')))
    local('pip install -r {}'.format(rfile))

def install_supervisor_configs():
    supervisor_conf_dir = '/etc/supervisor/conf.d'
    with lcd(supervisor_dir):
        local('mv * {}'.format(supervisor_conf_dir))

def install_startup_scripts():
    venv = os.path.join(venv_dir, app_name, 'bin')
    with lcd(scripts_dir):
        local('mv * {}'.format(venv))

if __name__ == '__main__':
    pull_git()
    create_venv()
    install_pip_requirements()
    install_supervisor_configs()
    install_startup_scripts()