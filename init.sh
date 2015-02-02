#! /bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip ssh autossh python-crypto

sudo pip install ecdsa paramiko
sudo pip install fabric
python ./fab.py
