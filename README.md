## Installation (Ubuntu 20.04)

1. Create an `A record` pointing to your server `ip`.

2. Run the installation script:

```bash
sudo apt update && sudo apt upgrade
cd
git clone https://github.com/cschlay/slippery.git
cd slippery
sudo ./scripts/install.sh
```

## Updating

```bash
cd slippery
sudo ./scripts/update.sh
```

## Users

### Create a user
```bash
# Create user
cd slippery
source venv/bin/activate
python3 manage.py createsuperuser
```

### Reset Lockout
```bash
cd slippery
source venv/bin/activate
python3 manage.py axes_reset
```
