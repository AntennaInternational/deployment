__author__ = 'brendan'
from fabric.api import *
import os
config_dir = os.path.join(os.path.dirname(__file__), 'sites-enabled')

def enable_webapp_config():
    with lcd(config_dir):
        local('cp * /etc/nginx/sites-enabled')

if __name__ == '__main__':
    enable_webapp_config()