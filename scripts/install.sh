#!/bin/bash

# Assumes that this project lives in the $HOME directory.

# It is users responsibility to update the system.
# The user should run "sudo apt update && sudo apt upgrade".
# It is not included in the script as it may break user's systems.

echo "Installing dependencies..."
# Server
apt install nginx -y
# Lets encrypt
apt install software-properties-common
add-apt-repository universe
apt update

# Slippery app itself
apt install python3-pip -y
apt install python3-venv -y

mkdir scripts/files
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Creates
# - slippery.service
echo "Creating configuration files..."
python3 scripts/install.py

echo "Preparing gunicorn..."
cp scripts/slippery.service /etc/systemd/system/slippery.service
systemctl daemon-reload
systemctl start slippery
systemctl enable slippery
systemctl status slippery

cp scripts/files/nginx-site-slippery /etc/nginx/sites-available/slippery
ln -s /etc/nginx/sites-available/slippery /etc/nginx/sites-enabled
systemctl restart nginx

cp scripts/files/sudoers-slippery /etc/sudoers.d/slippery

apt install certbot python3-certbot-nginx
certbot --nginx

python3 manage.py migrate
python3 manage.py createsuperuser
