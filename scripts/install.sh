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

# Postgres
apt install gcc -y
apt install libpq-dev -y
apt install postgresql

# Docker
# https://docs.docker.com/engine/install/ubuntu/
apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
apt update
apt install docker-ce docker-ce-cli containerd.io

# Docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

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

cp scripts/files/nginx-site-slippery /etc/nginx/sites-available/slippery
ln -s /etc/nginx/sites-available/slippery /etc/nginx/sites-enabled
systemctl restart nginx

cp scripts/files/sudoers-slippery /etc/sudoers.d/slippery

certbot --nginx

python3 manage.py migrate
chown $SUDO_USER:$SUDO_USER db.slite3
python3 manage.py createsuperuser

systemctl restart slippery
