#!/bin/bash

git pull
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
systemctl restart slippery
