#!/bin/bash

git pull
python3 manage.py migrate
systemctl restart slippery
