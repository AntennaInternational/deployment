#! /bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip
sudo pip install fabric
python ./fab.py