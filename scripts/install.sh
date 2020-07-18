#!/bin/bash

# Assumes that this project lives in the $HOME directory.

# It is users responsibility to update the system.
# The user should run "sudo apt update && sudo apt upgrade".
# It is not included in the script as it may break user's systems.

echo "Installing dependencies..."
# Server
apt install nginx -y
# Lets encrypt
apt install software-properties-common -y
apt install certbot python3-certbot-nginx -y
add-apt-repository universe
apt update

# Python Dependencies
apt install python3-pip -y
apt install python3-dev -y
apt install python3-venv -y

# Postgres Dependencies
apt install gcc -y
apt install libpq-dev -y

# Slippery app itself
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

python3 manage.py migrate
chown $SUDO_USER:$SUDO_USER db.sqlite3
python3 manage.py createsuperuser

certbot --nginx
systemctl restart slippery
