__author__ = 'brendan'
from fabric.api import *
import os
config_dir = os.path.join(os.path.dirname(__file__), 'sites-enabled')

def enable_webapp_config():
    with lcd(config_dir):
        local('cp * /etc/nginx/sites-enabled')
        local('cp * /etc/nginx/sites-available')
    local('rm -f /etc/nginx/sites-enabled/default')
    local('rm -f /etc/nginx/sites-available/default')

if __name__ == '__main__':
    enable_webapp_config()