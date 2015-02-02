#! /bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo groupadd webapps
sudo usermod -G webapps antenna
sudo apt-get install python-pip ssh autossh python-crypto

sudo pip install ecdsa paramiko
sudo pip install fabric
python ./fab.py
python ./server/fab.py
python ./webapp/fab.py
python ./redis/fab.py
python ./celery/fab.py

