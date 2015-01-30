__author__ = 'brendan'
from fabric.api import cd, lcd, local
import os

scripts_dir = os.path.join(os.path.dirname(__file__), 'sh')
supervisor_dir = os.path.join(os.path.dirname(__file__), 'supervisor')
venv_dir = '/webapps/venvs/rack_webapp'

def install_startup_scripts():
    bin_dir = os.path.join(venv_dir, 'bin')
    with lcd(scripts_dir):
        local('mv * {}'.format(bin_dir))

def install_supervisor_configs():
    supervisor_conf_dir = '/etc/supervisor/conf.d'
    with lcd(supervisor_dir):
        local('cp * {}'.format(supervisor_conf_dir))

if __name__ == '__main__':
    install_supervisor_configs()
    install_startup_scripts()