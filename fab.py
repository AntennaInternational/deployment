from fabric.api import local, settings
import os

system_dependancies = [
    "git",
    "supervisor",
    "autossh",
    "build-essential",
    "tcl8.5",
    "mysql-server",
    "mysql-client",
    "libmysqlclient-dev"
]

python_dependancies = [
    "virtualenv"
]

system_directories = [
    "/webapps",
    "/webapps/venvs",
    "/tmp"
]

def make_directories(dirs):
    for directory in dirs:
        local('mkdir -p {}'.format(directory))

def install_system_requirements(requirements):
    for req in requirements:
        local('apt-get install {}'.format(req))

def install_python_requirements(requirements):
    for req in requirements:
        with settings(warn_only=True, capture=True):
            result = local('pip install {}'.format(req))
        if result.failed:
            print 'Ignoring PIP error'

if __name__ == '__main__':
    make_directories(system_directories)
    install_system_requirements(system_dependancies)
    install_python_requirements(python_dependancies)
